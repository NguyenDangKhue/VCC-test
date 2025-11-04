# Viettel Construction - Chi nhánh Lâm Đồng (Web giới thiệu)

Ứng dụng web Python (Flask) giao diện hiện đại với chủ đạo đỏ - trắng. Bao gồm: Trang chủ, Danh mục sản phẩm, Danh mục hình ảnh.

## Chạy dự án (Windows PowerShell)

```powershell
cd D:\Viettel-construction\web-Test
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Mở trình duyệt: http://localhost:5000

## Cấu trúc thư mục

```
web-Test/
├─ app.py
├─ requirements.txt
├─ templates/
│  ├─ base.html
│  ├─ index.html
│  ├─ products.html
│  └─ gallery.html
├─ static/
│  ├─ css/styles.css
│  ├─ js/main.js
│  ├─ images/           # ảnh minh họa sản phẩm & gallery
│  └─ logo/             # đặt logo (.jfif) tại đây
└─ README.md
```

## Logo

- Đặt file logo định dạng `.jfif` vào thư mục `static/logo/`. Ứng dụng sẽ tự phát hiện file đầu tiên.

## Ảnh minh họa

- Thêm ảnh vào `static/images/` với tên khớp trong `app.py` hoặc sửa dữ liệu mẫu trong route tương ứng.

## Triển khai trên Render

1) Kết nối repo này với Render (Create New → Web Service → Connect Repository)

2) Render sẽ tự đọc `render.yaml` và đề xuất cấu hình. Kiểm tra:
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn "app:create_app()"`
   - Environment:
     - `APP_SECRET_KEY`: auto-generate (đã cấu hình trong render.yaml)
     - `PYTHON_VERSION`: 3.11.9
   - Persistent Disk:
     - Tên: `app-data`
     - Mount Path: `/opt/render/project/src/data`
     - Size: >= 1GB (tùy nhu cầu lưu file upload)

3) Deploy. Ứng dụng dùng `data/` để lưu `users.json` và file upload; Render disk đảm bảo dữ liệu không mất khi redeploy.

Ghi chú:
- Các file tĩnh và trang public nằm trong `static/` và `templates/`, phục vụ trực tiếp qua Flask.
- Nếu cần domain riêng, cấu hình Custom Domain trong Render.


