"""
Script de resize va compress cac hinh anh da co san trong thu muc projects.
Giam do phan giai xuong 1920x1080 va nen voi quality 80% de tiet kiem dung luong.
"""

from pathlib import Path
from PIL import Image
import os
import shutil
import sys

# Fix encoding for Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def resize_and_compress_image_file(image_path, max_width=1920, max_height=1080, quality=80):
    """
    Resize và compress một file hình ảnh.
    
    Args:
        image_path: Đường dẫn đến file hình ảnh
        max_width: Chiều rộng tối đa (mặc định 1920px)
        max_height: Chiều cao tối đa (mặc định 1080px)
        quality: Chất lượng JPEG từ 1-100 (mặc định 80)
    
    Returns:
        Tuple (success: bool, original_size: int, new_size: int, saved_bytes: int)
    """
    try:
        original_size = os.path.getsize(image_path)
        
        # Mở hình ảnh
        img = Image.open(image_path)
        original_mode = img.mode
        
        # Convert RGBA sang RGB nếu cần (để lưu JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Tạo background trắng cho ảnh có alpha channel
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Tính toán kích thước mới (giữ nguyên tỷ lệ)
        original_width, original_height = img.size
        ratio = min(max_width / original_width, max_height / original_height)
        
        # Chỉ resize nếu ảnh lớn hơn kích thước tối đa
        if ratio < 1:
            new_width = int(original_width * ratio)
            new_height = int(original_height * ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Tạo file tạm
        temp_path = str(image_path) + '.tmp'
        
        # Lưu với compression
        img.save(temp_path, format='JPEG', quality=quality, optimize=True)
        
        # Kiểm tra kích thước file mới
        new_size = os.path.getsize(temp_path)
        
        # Chỉ thay thế nếu file mới nhỏ hơn file cũ
        if new_size < original_size:
            # Backup file cũ (tùy chọn - có thể bỏ qua nếu muốn)
            # backup_path = str(image_path) + '.backup'
            # shutil.copy2(image_path, backup_path)
            
            # Thay thế file cũ
            shutil.move(temp_path, image_path)
            saved_bytes = original_size - new_size
            return True, original_size, new_size, saved_bytes
        else:
            # Xóa file tạm nếu không nhỏ hơn
            os.remove(temp_path)
            return False, original_size, original_size, 0
            
    except Exception as e:
        print(f"Loi khi xu ly {image_path}: {str(e)}")
        # Xóa file tạm nếu có
        temp_path = str(image_path) + '.tmp'
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return False, 0, 0, 0


def process_directory(directory_path):
    """
    Xử lý tất cả hình ảnh trong một thư mục.
    """
    directory = Path(directory_path)
    if not directory.exists():
        print(f"Thu muc khong ton tai: {directory_path}")
        return
    
    # Tìm tất cả file hình ảnh
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.jfif'}
    image_files = [f for f in directory.iterdir() 
                   if f.is_file() and f.suffix.lower() in image_extensions]
    
    if not image_files:
        print("Khong tim thay file hinh anh nao trong thu muc.")
        return
    
    print(f"Tim thay {len(image_files)} file hinh anh.")
    print("Bat dau xu ly...\n")
    
    total_original = 0
    total_new = 0
    total_saved = 0
    processed = 0
    skipped = 0
    errors = 0
    
    for image_file in image_files:
        print(f"Dang xu ly: {image_file.name}...", end=" ")
        
        success, orig_size, new_size, saved = resize_and_compress_image_file(image_file)
        
        if success:
            total_original += orig_size
            total_new += new_size
            total_saved += saved
            processed += 1
            saved_mb = saved / (1024 * 1024)
            reduction = (saved / orig_size * 100) if orig_size > 0 else 0
            print(f"OK - Da giam {saved_mb:.2f} MB ({reduction:.1f}%)")
        elif orig_size > 0:
            total_original += orig_size
            total_new += orig_size
            skipped += 1
            print("SKIP - File da toi uu hoac khong the xu ly")
        else:
            errors += 1
            print("ERROR")
    
    # Thống kê
    print("\n" + "="*60)
    print("THONG KE:")
    print(f"  - Tong so file: {len(image_files)}")
    print(f"  - Da xu ly thanh cong: {processed}")
    print(f"  - Bo qua: {skipped}")
    print(f"  - Loi: {errors}")
    print(f"\nDUNG LUONG:")
    total_orig_mb = total_original / (1024 * 1024)
    total_new_mb = total_new / (1024 * 1024)
    total_saved_mb = total_saved / (1024 * 1024)
    print(f"  - Dung luong ban dau: {total_orig_mb:.2f} MB")
    print(f"  - Dung luong sau xu ly: {total_new_mb:.2f} MB")
    if total_original > 0:
        print(f"  - Da tiet kiem: {total_saved_mb:.2f} MB ({total_saved/total_original*100:.1f}%)")
    print("="*60)


if __name__ == "__main__":
    import sys
    
    # Đường dẫn đến thư mục cần xử lý
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = r"D:\Build-WEB\VCC-test\data\uploads\projects\171dd8822f2542fcbfdac04be4e6c504"
    
    print("="*60)
    print("SCRIPT RESIZE VA COMPRESS HINH ANH")
    print("="*60)
    print(f"\nThu muc dich: {target_directory}")
    print("\nThong so:")
    print("  - Kich thuoc toi da: 1920x1080 (Full HD)")
    print("  - Chat luong JPEG: 80%")
    print("  - Format: JPEG")
    print("\nLuu y: File goc se duoc thay the bang file da xu ly.")
    print("="*60 + "\n")
    
    # Xác nhận (chỉ khi chạy interactive)
    if sys.stdin.isatty():
        try:
            confirm = input("Ban co muon tiep tuc? (yes/no): ").strip().lower()
            if confirm not in ['yes', 'y']:
                print("Da huy.")
                exit()
        except (EOFError, KeyboardInterrupt):
            print("\nDa huy.")
            exit()
    else:
        print("Chay tu dong (khong can xac nhan)...")
    
    process_directory(target_directory)
    print("\nHoan thanh!")

