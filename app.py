from flask import Flask, render_template, url_for, request, redirect, session, flash
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask import send_from_directory, abort
import json
import os
import uuid
from datetime import datetime


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")
    app.config['SECRET_KEY'] = os.environ.get('APP_SECRET_KEY', 'dev-secret-key-change-me')
    app.config['UPLOAD_FOLDER'] = str(Path("data") / "uploads")
    Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    users_file = data_dir / "users.json"
    customers_file = data_dir / "customers.json"

    def load_users():
        if users_file.exists():
            with open(users_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_users(users):
        with open(users_file, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

    def load_customers():
        if customers_file.exists():
            with open(customers_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_customers(customers):
        with open(customers_file, "w", encoding="utf-8") as f:
            json.dump(customers, f, ensure_ascii=False, indent=2)

    def ensure_admin():
        users = load_users()
        if "admin" not in users:
            users["admin"] = {
                "password": generate_password_hash("123"),
                "role": "admin",
                "full_name": "Administrator",
                "active": True,
            }
            save_users(users)

    ensure_admin()

    @app.context_processor
    def inject_branding():
        # Try to detect a logo in static/logo with .jfif extension
        logo_dir = Path(app.static_folder) / "logo"
        logo_path = None
        if logo_dir.exists():
            for ext in (".jfif", ".jfif".upper(), ".jpg", ".png", ".jpeg", ".webp"):
                candidates = list(logo_dir.glob(f"*{ext}"))
                if candidates:
                    # Take the first match
                    logo_path = f"logo/{candidates[0].name}"
                    break
        return {
            "brand_name": "Viettel Construction - Chi nhánh Lâm Đồng",
            "brand_logo": logo_path,
            "auth_user": current_user(),
        }

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/san-pham")
    def products():
        # Demo data; replace with real products later
        product_list = [
            {"name": "Giải pháp hạ tầng viễn thông", "desc": "Thi công, bảo trì, tối ưu hạ tầng.", "image": "images/sample-product-1.jpg"},
            {"name": "Năng lượng xanh", "desc": "Hệ thống điện mặt trời cho doanh nghiệp và hộ gia đình.", "image": "images/sample-product-2.jpg"},
            {"name": "Giải pháp tòa nhà thông minh", "desc": "Triển khai hệ thống IoT, M&E, an ninh.", "image": "images/sample-product-3.jpg"},
        ]
        return render_template("products.html", products=product_list)

    @app.route("/hinh-anh")
    def gallery():
        # Demo gallery; replace with real images later
        gallery_images = [
            "images/gallery-1.jpg",
            "images/gallery-2.jpg",
            "images/gallery-3.jpg",
            "images/gallery-4.jpg",
            "images/gallery-5.jpg",
            "images/gallery-6.jpg",
        ]
        return render_template("gallery.html", images=gallery_images)

    # -------- Authentication helpers & routes --------
    def current_user():
        username = session.get("username")
        if not username:
            return None
        users = load_users()
        user = users.get(username)
        if user and user.get("active"):
            return {"username": username, **user}
        return None

    def login_required(view_func):
        from functools import wraps
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            if not current_user():
                flash("Vui lòng đăng nhập để truy cập khu vực nội bộ.", "warning")
                return redirect(url_for("login", next=request.path))
            return view_func(*args, **kwargs)
        return wrapped

    def admin_required(view_func):
        from functools import wraps
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            user = current_user()
            if not user:
                flash("Vui lòng đăng nhập.", "warning")
                return redirect(url_for("login", next=request.path))
            if user.get("role") != "admin":
                flash("Bạn không có quyền truy cập chức năng này.", "danger")
                return redirect(url_for("dashboard"))
            return view_func(*args, **kwargs)
        return wrapped

    @app.route("/dang-nhap", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "")
            users = load_users()
            user = users.get(username)
            if user and user.get("active") and check_password_hash(user.get("password", ""), password):
                session["username"] = username
                flash("Đăng nhập thành công!", "success")
                dest = request.args.get("next") or url_for("dashboard")
                return redirect(dest)
            flash("Sai tài khoản hoặc mật khẩu.", "danger")
        return render_template("auth/login.html")

    @app.route("/dang-xuat")
    def logout():
        session.pop("username", None)
        flash("Đã đăng xuất.", "info")
        return redirect(url_for("index"))

    # -------- Internal Area --------
    @app.route("/noi-bo")
    @login_required
    def dashboard():
        # Build "my tasks" for the logged-in user
        user = current_user()
        my_tasks = []
        customers = load_customers()
        for cust in customers:
            for it in cust.get("consultations", []):
                if it.get("nhan_vien") == user.get("username") and it.get("trang_thai") in ("cho_xac_nhan", "dang_xu_ly"):
                    my_tasks.append({
                        "customer_id": cust.get("ma_khach_hang"),
                        "customer_name": cust.get("ho_ten"),
                        "consult_id": it.get("id"),
                        "title": it.get("tieu_de"),
                        "status": it.get("trang_thai"),
                        "due": it.get("thoi_han"),
                        "created_at": it.get("created_at"),
                    })
        # sort newest first by created_at
        my_tasks.sort(key=lambda x: x.get("created_at") or "", reverse=True)
        return render_template("internal/dashboard.html", my_tasks=my_tasks)

    # User management (admin only)
    @app.route("/noi-bo/nguoi-dung")
    @admin_required
    def users_list():
        users = load_users()
        safe_users = [
            {"username": u, "role": v.get("role"), "full_name": v.get("full_name"), "active": v.get("active", True)}
            for u, v in users.items()
        ]
        return render_template("internal/users.html", users=safe_users)

    @app.route("/noi-bo/nguoi-dung/tao", methods=["POST"])
    @admin_required
    def users_create():
        username = request.form.get("username", "").strip()
        full_name = request.form.get("full_name", "").strip()
        role = request.form.get("role", "user")
        password = request.form.get("password", "")
        if not username or not password:
            flash("Vui lòng nhập tài khoản và mật khẩu.", "warning")
            return redirect(url_for("users_list"))
        users = load_users()
        if username in users:
            flash("Tài khoản đã tồn tại.", "danger")
            return redirect(url_for("users_list"))
        users[username] = {
            "password": generate_password_hash(password),
            "role": role,
            "full_name": full_name or username,
            "active": True,
        }
        save_users(users)
        flash("Tạo người dùng thành công.", "success")
        return redirect(url_for("users_list"))

    @app.route("/noi-bo/nguoi-dung/xoa/<username>", methods=["POST"])
    @admin_required
    def users_delete(username):
        if username == "admin":
            flash("Không thể xóa tài khoản quản trị mặc định.", "danger")
            return redirect(url_for("users_list"))
        users = load_users()
        if username in users:
            users.pop(username)
            save_users(users)
            flash("Đã xóa người dùng.", "info")
        return redirect(url_for("users_list"))

    @app.route("/noi-bo/nguoi-dung/dat-lai-mk/<username>", methods=["POST"])
    @admin_required
    def users_reset_password(username):
        new_password = request.form.get("new_password", "")
        if not new_password:
            flash("Vui lòng nhập mật khẩu mới.", "warning")
            return redirect(url_for("users_list"))
        users = load_users()
        if username in users:
            users[username]["password"] = generate_password_hash(new_password)
            save_users(users)
            flash("Đã đặt lại mật khẩu.", "success")
        return redirect(url_for("users_list"))

    # -------- Customers Module (internal - any logged-in user) --------
    CUSTOMER_TYPES_A = ["Nhà cấp 4", "Biệt thự", "Nhà phố", "Khác"]
    CUSTOMER_TYPES_B = [
        "Cải tạo sửa chữa",
        "Thi công hoàn thiện",
        "Thi công kết cấu thô",
        "Thi công trọn gói",
        "Trọn gói - chìa khóa trao tay",
        "Khác (nội thất)",
        "Khác (xây dựng)",
    ]
    CUSTOMER_TIEM_NANG = [
        "Cấp 1: rất tiềm năng, đang cần gấp",
        "Cấp 2: Tiềm năng, có nhu cầu thật, có khả năng chốt",
        "Cấp 3: Do dự, có nhu cầu thật, đang đi tham khảo",
        "Cấp 4 Đang tìm hiểu thông tin, chưa có nhu cầu thật",
    ]
    CUSTOMER_GIAI_DOAN = [
        "Liên hệ khách hàng",
        "Tiếp xúc trực tiếp",
        "Tư vấn phướng án, thiết kế",
        "Dự toán, báo giá",
        "Ký hợp đồng thi công",
        "Thành công",
    ]

    @app.route("/noi-bo/khach-hang")
    @login_required
    def customers_list():
        customers = load_customers()
        return render_template("internal/customers_list.html", customers=customers)

    def _find_customer(customers, ma_kh):
        for c in customers:
            if c.get("ma_khach_hang") == ma_kh:
                return c
        return None

    @app.route("/noi-bo/khach-hang/tao", methods=["GET", "POST"])
    @login_required
    def customers_create():
        if request.method == "POST":
            form = request.form
            record = {
                "ma_khach_hang": form.get("ma_khach_hang", "").strip(),
                "ho_ten": form.get("ho_ten", "").strip(),
                "so_dien_thoai": form.get("so_dien_thoai", "").strip(),
                "dia_chi": form.get("dia_chi", "").strip(),
                "dia_chi_thi_cong": form.get("dia_chi_thi_cong", "").strip(),
                "loai_cong_trinh_a": form.get("loai_cong_trinh_a", ""),
                "loai_cong_trinh_b": form.get("loai_cong_trinh_b", ""),
                "thoi_gian_du_kien": form.get("thoi_gian_du_kien", "").strip(),
                "quy_mo_ngan_sach": form.get("quy_mo_ngan_sach", "").strip(),
                "phan_cap_tiem_nang": form.get("phan_cap_tiem_nang", ""),
                "giai_doan_thuc_hien": form.get("giai_doan_thuc_hien", ""),
            }
            if not record["ma_khach_hang"] or not record["ho_ten"]:
                flash("Mã KH và Họ tên là bắt buộc.", "warning")
                return redirect(url_for("customers_create"))
            customers = load_customers()
            if any(c.get("ma_khach_hang") == record["ma_khach_hang"] for c in customers):
                flash("Mã khách hàng đã tồn tại.", "danger")
                return redirect(url_for("customers_create"))
            record["consultations"] = []
            customers.append(record)
            save_customers(customers)
            flash("Đã tạo khách hàng.", "success")
            return redirect(url_for("customers_list"))
        return render_template(
            "internal/customers_form.html",
            mode="create",
            customer={},
            TYPES_A=CUSTOMER_TYPES_A,
            TYPES_B=CUSTOMER_TYPES_B,
            TIEM_NANG=CUSTOMER_TIEM_NANG,
            GIAI_DOAN=CUSTOMER_GIAI_DOAN,
        )

    @app.route("/noi-bo/khach-hang/sua/<ma_kh>", methods=["GET", "POST"])
    @login_required
    def customers_edit(ma_kh):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        if request.method == "POST":
            form = request.form
            customer.update({
                "ho_ten": form.get("ho_ten", "").strip(),
                "so_dien_thoai": form.get("so_dien_thoai", "").strip(),
                "dia_chi": form.get("dia_chi", "").strip(),
                "dia_chi_thi_cong": form.get("dia_chi_thi_cong", "").strip(),
                "loai_cong_trinh_a": form.get("loai_cong_trinh_a", ""),
                "loai_cong_trinh_b": form.get("loai_cong_trinh_b", ""),
                "thoi_gian_du_kien": form.get("thoi_gian_du_kien", "").strip(),
                "quy_mo_ngan_sach": form.get("quy_mo_ngan_sach", "").strip(),
                "phan_cap_tiem_nang": form.get("phan_cap_tiem_nang", ""),
                "giai_doan_thuc_hien": form.get("giai_doan_thuc_hien", ""),
            })
            save_customers(customers)
            flash("Đã cập nhật khách hàng.", "success")
            return redirect(url_for("customers_list"))
        return render_template(
            "internal/customers_form.html",
            mode="edit",
            customer=customer,
            TYPES_A=CUSTOMER_TYPES_A,
            TYPES_B=CUSTOMER_TYPES_B,
            TIEM_NANG=CUSTOMER_TIEM_NANG,
            GIAI_DOAN=CUSTOMER_GIAI_DOAN,
        )

    @app.route("/noi-bo/khach-hang/xoa/<ma_kh>", methods=["POST"])
    @login_required
    def customers_delete(ma_kh):
        customers = load_customers()
        new_customers = [c for c in customers if c.get("ma_khach_hang") != ma_kh]
        if len(new_customers) != len(customers):
            save_customers(new_customers)
            flash("Đã xoá khách hàng.", "info")
        return redirect(url_for("customers_list"))

    # -------- Customer detail & consultations --------
    def _now_iso():
        return datetime.now().isoformat(timespec='seconds')

    def _find_consultation(customer, consult_id):
        for item in customer.get("consultations", []):
            if item.get("id") == consult_id:
                return item
        return None

    @app.route("/noi-bo/khach-hang/<ma_kh>")
    @login_required
    def customers_detail(ma_kh):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        users = load_users()
        return render_template("internal/customer_detail.html", customer=customer, users=users)

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/tao", methods=["POST"])
    @admin_required
    def consultation_create(ma_kh):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        form = request.form
        consult = {
            "id": uuid.uuid4().hex,
            "tieu_de": form.get("tieu_de", "").strip() or "Yêu cầu tư vấn",
            "nhan_vien": form.get("nhan_vien", "").strip(),
            "thoi_han": form.get("thoi_han", "").strip(),
            "ghi_chu": form.get("ghi_chu", "").strip(),
            "trang_thai": "cho_xac_nhan",
            "created_at": _now_iso(),
            "accepted_at": None,
            "completed_at": None,
            "ket_qua": "",
            "attachments": [],
        }
        customer.setdefault("consultations", []).append(consult)
        save_customers(customers)
        flash("Đã tạo yêu cầu tư vấn (chờ xác nhận).", "success")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/<consult_id>/ket-qua", methods=["POST"])
    @login_required
    def consultation_update_result(ma_kh, consult_id):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        item = _find_consultation(customer, consult_id)
        if not item:
            flash("Không tìm thấy yêu cầu.", "danger")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        item["ket_qua"] = (request.form.get("ket_qua") or "").strip()
        save_customers(customers)
        flash("Đã lưu ghi chú kết quả thực hiện.", "success")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/<consult_id>/nhan", methods=["POST"])
    @login_required
    def consultation_accept(ma_kh, consult_id):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        item = _find_consultation(customer, consult_id)
        if not item:
            flash("Không tìm thấy yêu cầu.", "danger")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        if item.get("trang_thai") == "cho_xac_nhan":
            item["trang_thai"] = "dang_xu_ly"
            item["accepted_at"] = _now_iso()
            item["accepted_by"] = session.get("username")
            save_customers(customers)
            flash("Đã nhận việc, chuyển sang đang xử lý.", "info")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/<consult_id>/hoan-thanh", methods=["POST"])
    @login_required
    def consultation_complete(ma_kh, consult_id):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        item = _find_consultation(customer, consult_id)
        if not item:
            flash("Không tìm thấy yêu cầu.", "danger")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        if item.get("trang_thai") in ("cho_xac_nhan", "dang_xu_ly"):
            item["trang_thai"] = "hoan_thanh"
            item["completed_at"] = _now_iso()
            item["completed_by"] = session.get("username")
            save_customers(customers)
            flash("Đã đánh dấu hoàn thành.", "success")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/<consult_id>/upload", methods=["POST"])
    @login_required
    def consultation_upload(ma_kh, consult_id):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        item = _find_consultation(customer, consult_id)
        if not item:
            flash("Không tìm thấy yêu cầu.", "danger")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        files = request.files.getlist("files")
        saved_any = False
        if files:
            uploads_root = Path(app.config['UPLOAD_FOLDER'])
            secure_ma = secure_filename(ma_kh)
            target_dir = uploads_root / secure_ma / consult_id
            target_dir.mkdir(parents=True, exist_ok=True)
            for f in files:
                if not f.filename:
                    continue
                filename = secure_filename(f.filename)
                dest = target_dir / filename
                f.save(str(dest))
                # Store path relative to uploads root with POSIX separators
                rel_path = f"{secure_ma}/{consult_id}/{filename}"
                item.setdefault("attachments", []).append({
                    "filename": filename,
                    "path": rel_path,
                    "uploaded_at": _now_iso(),
                    "uploader": session.get("username"),
                })
                saved_any = True
        if saved_any:
            save_customers(customers)
            flash("Đã tải lên tệp đính kèm.", "success")
        else:
            flash("Không có tệp hợp lệ.", "warning")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    @app.route("/uploads/<path:subpath>")
    @login_required
    def serve_upload(subpath):
        # Serve files under uploads root securely to logged-in users only
        uploads_root = Path(app.config['UPLOAD_FOLDER']).resolve()
        requested = (uploads_root / subpath).resolve()
        if not str(requested).startswith(str(uploads_root)) or not requested.exists():
            return abort(404)
        as_attachment = request.args.get("download") == "1"
        return send_from_directory(directory=str(uploads_root), path=subpath, as_attachment=as_attachment)

    @app.route("/noi-bo/khach-hang/<ma_kh>/tu-van/<consult_id>/xoa-tap-tin", methods=["POST"])
    @login_required
    def consultation_delete_attachment(ma_kh, consult_id):
        customers = load_customers()
        customer = _find_customer(customers, ma_kh)
        if not customer:
            flash("Không tìm thấy khách hàng.", "danger")
            return redirect(url_for("customers_list"))
        item = _find_consultation(customer, consult_id)
        if not item:
            flash("Không tìm thấy yêu cầu.", "danger")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        subpath = (request.form.get("path") or "").replace("\\", "/").replace("uploads/", "")
        if not subpath:
            flash("Thiếu đường dẫn tệp.", "warning")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        # Validate attachment exists in metadata
        attachments = item.get("attachments", [])
        match = None
        for a in attachments:
            ap = (a.get("path") or "").replace("\\", "/").replace("uploads/", "")
            if ap == subpath:
                match = a
                break
        if not match:
            flash("Không tìm thấy tệp trong danh sách đính kèm.", "warning")
            return redirect(url_for("customers_detail", ma_kh=ma_kh))
        # Remove file from disk (if exists within uploads root)
        uploads_root = Path(app.config['UPLOAD_FOLDER']).resolve()
        requested = (uploads_root / subpath).resolve()
        if str(requested).startswith(str(uploads_root)) and requested.exists():
            try:
                requested.unlink()
            except Exception:
                pass
        # Remove from metadata
        item["attachments"] = [a for a in attachments if a is not match]
        save_customers(customers)
        flash("Đã xoá tệp đính kèm.", "info")
        return redirect(url_for("customers_detail", ma_kh=ma_kh))

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


