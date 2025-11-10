document.addEventListener('DOMContentLoaded', function () {
  // Gallery project modal functionality
  const projects = window.galleryProjects || [];
  
  // Global function to open project modal (can be called from onclick)
  window.openProjectModal = function(projectId) {
    const project = projects.find(p => p.id === projectId);
    if (project) {
      // Get current filter value
      const selectedProgress = progressFilter ? progressFilter.value : '';
      showProjectModal(project, selectedProgress);
    }
  };
  
  // Check if there's a project parameter in URL (from hero click)
  const urlParams = new URLSearchParams(window.location.search);
  const projectParam = urlParams.get('project');
  if (projectParam) {
    // Scroll to gallery section and open modal
    setTimeout(() => {
      window.openProjectModal(projectParam);
      // Remove parameter from URL
      window.history.replaceState({}, document.title, window.location.pathname);
    }, 500);
  }
  
  // Handle "View Details" button clicks
  document.querySelectorAll('.view-project-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.stopPropagation(); // Prevent card click
      const projectId = this.getAttribute('data-project-id');
      window.openProjectModal(projectId);
    });
  });
  
  // Progress filter functionality
  const progressFilter = document.getElementById('progressFilter');
  const clearFilterBtn = document.getElementById('clearFilter');
  const projectCards = document.querySelectorAll('.project-card-wrapper');
  const projectCountEl = document.getElementById('projectCount');
  const noResultsEl = document.getElementById('noResults');
  const galleryContainer = document.getElementById('gallery-container');
  
  function filterProjects() {
    const selectedProgress = progressFilter ? progressFilter.value : '';
    let visibleCount = 0;
    
    projectCards.forEach(card => {
      const cardProgress = card.getAttribute('data-progress') || '';
      const progressList = cardProgress.split(',').map(p => p.trim());
      
      if (!selectedProgress || progressList.includes(selectedProgress)) {
        card.style.display = '';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });
    
    // Update count
    if (projectCountEl) {
      projectCountEl.textContent = visibleCount;
    }
    
    // Show/hide no results message
    if (noResultsEl && galleryContainer) {
      if (visibleCount === 0 && selectedProgress) {
        galleryContainer.style.display = 'none';
        noResultsEl.style.display = 'block';
      } else {
        galleryContainer.style.display = '';
        noResultsEl.style.display = 'none';
      }
    }
  }
  
  // Filter on change
  if (progressFilter) {
    progressFilter.addEventListener('change', filterProjects);
  }
  
  // Clear filter button
  if (clearFilterBtn) {
    clearFilterBtn.addEventListener('click', function() {
      if (progressFilter) {
        progressFilter.value = '';
        filterProjects();
      }
    });
  }
  
  // Filter by clicking on progress badge
  window.filterByProgress = function(progress) {
    if (progressFilter) {
      progressFilter.value = progress;
      filterProjects();
      // Scroll to filter section
      const filterSection = document.querySelector('.gallery-filters');
      if (filterSection) {
        filterSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  };

  // Show project modal with details
  function showProjectModal(project, filterProgress = '') {
    const modal = new bootstrap.Modal(document.getElementById('projectModal'));
    const content = document.getElementById('projectModalContent');
    
    // Always show project info
    let html = `
      <div class="project-detail-header">
        <h4>${escapeHtml(project.chu_dau_tu)}</h4>
        ${project.quy_mo_du_an ? `<p class="text-muted mb-1"><i class="bi bi-rulers"></i> ${escapeHtml(project.quy_mo_du_an)}</p>` : ''}
        <p class="text-muted mb-1"><i class="bi bi-geo-alt"></i> ${escapeHtml(project.dia_chi_du_an)}</p>
        ${project.ngay_khoi_cong ? `<p class="text-muted mb-0"><i class="bi bi-calendar-event"></i> Ngày khởi công: ${formatDate(project.ngay_khoi_cong)}</p>` : ''}
      </div>
    `;
    
    if (project.images && project.images.length > 0) {
      // Filter images by progress if filter is active
      let filteredImages = project.images;
      if (filterProgress) {
        filteredImages = project.images.filter(img => img.progress === filterProgress);
      }
      
      if (filteredImages.length > 0) {
        // Show filter indicator if filtering
        if (filterProgress) {
          html += `
            <div class="alert alert-info d-flex align-items-center mb-3">
              <i class="bi bi-funnel-fill me-2"></i>
              <span>Đang hiển thị <strong>${filteredImages.length}</strong> hình ảnh thuộc tiến độ: <strong>${escapeHtml(filterProgress)}</strong></span>
            </div>
          `;
        }
        
        html += '<div class="project-images-grid">';
        filteredImages.forEach(image => {
          const imageUrl = `/uploads/projects/${project.id}/${image.filename}`;
          html += `
            <div class="project-image-item" onclick="openLightbox('${imageUrl}', '${escapeHtml(image.progress)}')">
              <img src="${imageUrl}" alt="${escapeHtml(image.progress)}" loading="lazy">
              <div class="image-progress">${escapeHtml(image.progress)}</div>
            </div>
          `;
        });
        html += '</div>';
      } else {
        // No images match the filter
        if (filterProgress) {
          html += `
            <div class="alert alert-warning">
              <i class="bi bi-exclamation-triangle me-2"></i>
              Dự án này không có hình ảnh nào thuộc tiến độ: <strong>${escapeHtml(filterProgress)}</strong>
            </div>
          `;
        } else {
          html += '<div class="alert alert-info">Chưa có hình ảnh nào trong dự án này.</div>';
        }
      }
    } else {
      html += '<div class="alert alert-info">Chưa có hình ảnh nào trong dự án này.</div>';
    }
    
    content.innerHTML = html;
    modal.show();
  }

  // Escape HTML to prevent XSS
  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Format date from YYYY-MM-DD to DD/MM/YYYY
  function formatDate(dateString) {
    if (!dateString) return '';
    const parts = dateString.split('-');
    if (parts.length === 3) {
      return `${parts[2]}/${parts[1]}/${parts[0]}`;
    }
    return escapeHtml(dateString);
  }

  // Lightbox functionality
  window.openLightbox = function(imageUrl, progress) {
    // Create lightbox if it doesn't exist
    let lightbox = document.getElementById('imageLightbox');
    if (!lightbox) {
      lightbox = document.createElement('div');
      lightbox.id = 'imageLightbox';
      lightbox.className = 'image-lightbox';
      lightbox.innerHTML = `
        <button class="close-lightbox" onclick="closeLightbox()">&times;</button>
        <img src="" alt="">
      `;
      document.body.appendChild(lightbox);
      
      // Close on background click
      lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
          closeLightbox();
        }
      });
      
      // Close on ESC key
      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
          closeLightbox();
        }
      });
    }
    
    const img = lightbox.querySelector('img');
    img.src = imageUrl;
    img.alt = progress || 'Hình ảnh dự án';
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  window.closeLightbox = function() {
    const lightbox = document.getElementById('imageLightbox');
    if (lightbox) {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
    }
  };
});
