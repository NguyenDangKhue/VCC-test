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
    projects_file = data_dir / "construction_projects.json"
    progress_options_file = data_dir / "progress_options.json"
    hang_muc_file = data_dir / "hang_muc.json"
    gia_xay_tho_file = data_dir / "gia_xay_tho.json"
    gia_hoan_thien_file = data_dir / "gia_hoan_thien.json"
    vat_tu_file = data_dir / "vat_tu.json"
    hero_images_file = data_dir / "hero_images.json"
    administrative_units_file = data_dir / "administrative_units.json"

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

    def load_projects():
        if projects_file.exists():
            with open(projects_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_projects(projects):
        with open(projects_file, "w", encoding="utf-8") as f:
            json.dump(projects, f, ensure_ascii=False, indent=2)

    def load_progress_options():
        if progress_options_file.exists():
            with open(progress_options_file, "r", encoding="utf-8") as f:
                return json.load(f)
        # Default progress options
        default_options = [
            "Tư vấn khách hàng",
            "Ký kết hợp đồng",
            "Khởi công",
            "Hệ cọc móng",
            "Đổ sàn",
            "Xây tường vây",
            "Tô tường",
            "Điện nước",
            "Hoàn thiện"
        ]
        save_progress_options(default_options)
        return default_options

    def save_progress_options(options):
        with open(progress_options_file, "w", encoding="utf-8") as f:
            json.dump(options, f, ensure_ascii=False, indent=2)

    def load_hang_muc():
        if hang_muc_file.exists():
            with open(hang_muc_file, "r", encoding="utf-8") as f:
                return json.load(f)
        # Default hang muc
        default_hang_muc = [
            {"id": "ket_cau_mong", "name": "Kết cấu móng", "he_so": 0.4, "order": 1},
            {"id": "tang_ham", "name": "Tầng hầm", "he_so": 1.5, "order": 2},
            {"id": "tang_tret", "name": "Tầng trệt", "he_so": 1, "order": 3},
            {"id": "tang_1", "name": "Tầng 1", "he_so": 1, "order": 4},
            {"id": "tang_2", "name": "Tầng 2", "he_so": 1, "order": 5},
            {"id": "tang_3", "name": "Tầng 3", "he_so": 1, "order": 6},
            {"id": "tang_4", "name": "Tầng 4", "he_so": 1, "order": 7},
            {"id": "tang_5", "name": "Tầng 5", "he_so": 1, "order": 8},
            {"id": "tang_6", "name": "Tầng 6", "he_so": 1, "order": 9},
            {"id": "tang_lung", "name": "Tầng lửng", "he_so": 1, "order": 10},
            {"id": "mai_chinh", "name": "Mái chính + mái che sân thượng", "he_so": 0.2, "order": 11},
            {"id": "san_thuong", "name": "Sân thượng", "he_so": 1, "order": 12},
        ]
        save_hang_muc(default_hang_muc)
        return default_hang_muc

    def save_hang_muc(hang_muc):
        with open(hang_muc_file, "w", encoding="utf-8") as f:
            json.dump(hang_muc, f, ensure_ascii=False, indent=2)

    def load_gia_xay_tho():
        if gia_xay_tho_file.exists():
            with open(gia_xay_tho_file, "r", encoding="utf-8") as f:
                return json.load(f)
        # Default gia
        default_gia = [
            {"id": "gia_1", "gia": 3650000, "mo_ta": "3.650.000 VNĐ/m²", "active": True, "order": 1},
            {"id": "gia_2", "gia": 3950000, "mo_ta": "3.950.000 VNĐ/m²", "active": True, "order": 2},
        ]
        save_gia_xay_tho(default_gia)
        return default_gia

    def save_gia_xay_tho(gia_list):
        with open(gia_xay_tho_file, "w", encoding="utf-8") as f:
            json.dump(gia_list, f, ensure_ascii=False, indent=2)

    def load_gia_hoan_thien():
        if gia_hoan_thien_file.exists():
            with open(gia_hoan_thien_file, "r", encoding="utf-8") as f:
                return json.load(f)
        # Default gia hoan thien
        default_gia = [
            {"id": "gia_ht_1", "gia": 2150000, "mo_ta": "2.150.000 VNĐ/m²", "active": True, "order": 1},
            {"id": "gia_ht_2", "gia": 2650000, "mo_ta": "2.650.000 VNĐ/m²", "active": True, "order": 2},
            {"id": "gia_ht_3", "gia": 3150000, "mo_ta": "3.150.000 VNĐ/m²", "active": True, "order": 3},
            {"id": "gia_ht_4", "gia": 3650000, "mo_ta": "3.650.000 VNĐ/m²", "active": True, "order": 4},
        ]
        save_gia_hoan_thien(default_gia)
        return default_gia

    def save_gia_hoan_thien(gia_list):
        with open(gia_hoan_thien_file, "w", encoding="utf-8") as f:
            json.dump(gia_list, f, ensure_ascii=False, indent=2)

    def load_vat_tu():
        if vat_tu_file.exists():
            with open(vat_tu_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Migrate old format to new format if needed
                if "xay_tho" not in data and "hoan_thien" not in data:
                    # Old format - migrate to new format
                    migrated = {
                        "xay_tho": {},
                        "hoan_thien": {}
                    }
                    for key, value in data.items():
                        migrated["xay_tho"][key] = value
                    # Add hoan thien data
                    try:
                        import sys
                        from pathlib import Path
                        sys.path.insert(0, str(Path(__file__).parent / "data"))
                        from vat_tu_hoan_thien_default import get_default_hoan_thien_data
                        migrated["hoan_thien"] = get_default_hoan_thien_data()
                    except Exception:
                        migrated["hoan_thien"] = {}
                    save_vat_tu(migrated)
                    return migrated
                # Ensure hoan_thien exists and has data
                if "hoan_thien" not in data or not data["hoan_thien"]:
                    try:
                        import sys
                        from pathlib import Path
                        sys.path.insert(0, str(Path(__file__).parent / "data"))
                        from vat_tu_hoan_thien_default import get_default_hoan_thien_data
                        data["hoan_thien"] = get_default_hoan_thien_data()
                        save_vat_tu(data)
                    except Exception:
                        if "hoan_thien" not in data:
                            data["hoan_thien"] = {}
                return data
        # Default vat tu data - new structure with xay_tho and hoan_thien
        default_vat_tu = {
            "xay_tho": {
                "3650000": {
                "gia": 3650000,
                "mo_ta": "3.650.000 VNĐ/m²",
                "categories": [
                    {
                        "name": "I. Vật tư thô",
                        "items": [
                            {"ten": "Xi măng", "chi_tiet": "Holcim (Hà Tiên/Kiên Lương)"},
                            {"ten": "Cát", "chi_tiet": "Cát bê tông (Hạt lớn, sạch), Cát xây tô (Mịn, sạch)"},
                            {"ten": "Đá", "chi_tiet": "Đá 1x2 (Bê tông), Đá 4x6 (Lăm le móng)"},
                            {"ten": "Thép", "chi_tiet": "Việt Nhật/Pomina"},
                            {"ten": "Gạch", "chi_tiet": "Tuynel (Đồng Nai/Bình Dương)"}
                        ]
                    },
                    {
                        "name": "II. Hệ thống kỹ thuật",
                        "items": [
                            {"ten": "Ống nước lạnh", "chi_tiet": "Bình Minh - Phi 21, 27, 42, 49"},
                            {"ten": "Ống nước nóng", "chi_tiet": "Bình Minh - Phi 21, 27"},
                            {"ten": "Ống thoát nước", "chi_tiet": "Bình Minh - Phi 42, 48, 60, 90, 114"},
                            {"ten": "Ống luồn dây điện", "chi_tiet": "PVC Ống ruột gà"},
                            {"ten": "Dây điện", "chi_tiet": "Cadivi/Dây Tivi"},
                            {"ten": "Dây tín hiệu", "chi_tiet": "Internet/TV (Sino/Comet)"}
                        ]
                    },
                    {
                        "name": "III. Hóa chất & Phụ gia",
                        "items": [
                            {"ten": "Chống thấm", "chi_tiet": "Sika/Fosmix (sàn WC, sê nô)"},
                            {"ten": "Bột trét tường", "chi_tiet": "Thành phần chính"}
                        ]
                    },
                    {
                        "name": "IV. Dịch vụ và Chính sách",
                        "items": [
                            {"ten": "Nhân công", "chi_tiet": "Cung cấp nhân công hoàn thiện"},
                            {"ten": "Ván khuôn", "chi_tiet": "Ván khuôn, cây chống (Đà Lạt thông)"},
                            {"ten": "Bảo hành kết cấu", "chi_tiet": "5 NĂM"},
                            {"ten": "Bảo hành thấm dột", "chi_tiet": "Có"},
                            {"ten": "Vệ sinh công nghiệp", "chi_tiet": "Không áp dụng"},
                            {"ten": "Hồ sơ và Pháp lý", "chi_tiet": "Hỗ trợ pháp lý, xin phép xây dựng, thủ tục hoàn công"},
                            {"ten": "Quản lý", "chi_tiet": "Cung cấp đầy đủ hồ sơ, tiến độ thi công, nhật ký công trình"},
                            {"ten": "Khác", "chi_tiet": "Trang bị bảo hộ, bảo hiểm y tế, khảo sát trước/sau thi công"}
                        ]
                    }
                ]
            },
                "3950000": {
                    "gia": 3950000,
                    "mo_ta": "3.950.000 VNĐ/m²",
                    "categories": [
                        {
                            "name": "I. Vật tư thô",
                            "items": [
                                {"ten": "Xi măng", "chi_tiet": "Holcim (Hà Tiên/Kiên Lương)"},
                                {"ten": "Cát", "chi_tiet": "Cát bê tông (Hạt lớn, sạch), Cát xây tô (Mịn, sạch)"},
                                {"ten": "Đá", "chi_tiet": "Đá 1x2 (Bê tông), Đá 4x6 (Lăm le móng)"},
                                {"ten": "Thép", "chi_tiet": "Việt Nhật/Pomina"},
                                {"ten": "Gạch", "chi_tiet": "Tuynel (Đồng Nai/Bình Dương)"}
                            ]
                        },
                        {
                            "name": "II. Hệ thống kỹ thuật",
                            "items": [
                                {"ten": "Ống nước lạnh", "chi_tiet": "Bình Minh - Phi 21, 27, 42, 49"},
                                {"ten": "Ống nước nóng", "chi_tiet": "Bình Minh - Phi 21, 27"},
                                {"ten": "Ống thoát nước", "chi_tiet": "Bình Minh - Phi 42, 48, 60, 90, 114"},
                                {"ten": "Ống luồn dây điện", "chi_tiet": "PVC Ống ruột gà"},
                                {"ten": "Dây điện", "chi_tiet": "Cadivi/Dây Tivi"},
                                {"ten": "Dây tín hiệu", "chi_tiet": "Internet/TV (Sino/Comet)"}
                            ]
                        },
                        {
                            "name": "III. Hóa chất & Phụ gia",
                            "items": [
                                {"ten": "Chống thấm", "chi_tiet": "Sika/Fosmix (sàn WC, sê nô)"},
                                {"ten": "Bột trét tường", "chi_tiet": "Thành phần chính"}
                            ]
                        },
                        {
                            "name": "IV. Dịch vụ và Chính sách",
                            "items": [
                                {"ten": "Nhân công", "chi_tiet": "Cung cấp nhân công hoàn thiện"},
                                {"ten": "Ván khuôn", "chi_tiet": "Ván khuôn, cây chống (Đà Lạt thông)"},
                                {"ten": "Bảo hành kết cấu", "chi_tiet": "10 NĂM"},
                                {"ten": "Bảo hành thấm dột", "chi_tiet": "Có"},
                                {"ten": "Vệ sinh công nghiệp", "chi_tiet": "Có (Áp dụng)"},
                                {"ten": "Hồ sơ và Pháp lý", "chi_tiet": "Hỗ trợ pháp lý, xin phép xây dựng, thủ tục hoàn công"},
                                {"ten": "Quản lý", "chi_tiet": "Cung cấp đầy đủ hồ sơ, tiến độ thi công, nhật ký công trình"},
                                {"ten": "Khác", "chi_tiet": "Trang bị bảo hộ, bảo hiểm y tế, khảo sát trước/sau thi công"}
                            ]
                        }
                    ]
                }
            }
        }
        # Import hoan thien data
        try:
            import sys
            from pathlib import Path
            sys.path.insert(0, str(Path(__file__).parent / "data"))
            from vat_tu_hoan_thien_default import get_default_hoan_thien_data
            default_vat_tu["hoan_thien"] = get_default_hoan_thien_data()
        except Exception as e:
            # If import fails, use empty dict
            default_vat_tu["hoan_thien"] = {}
        save_vat_tu(default_vat_tu)
        return default_vat_tu

    def save_vat_tu(vat_tu_data):
        with open(vat_tu_file, "w", encoding="utf-8") as f:
            json.dump(vat_tu_data, f, ensure_ascii=False, indent=2)

    def load_hero_images():
        if hero_images_file.exists():
            with open(hero_images_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def load_administrative_units():
        if administrative_units_file.exists():
            with open(administrative_units_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_hero_images(hero_images):
        with open(hero_images_file, "w", encoding="utf-8") as f:
            json.dump(hero_images, f, ensure_ascii=False, indent=2)

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
        hero_images = load_hero_images()
        # Load project details for hero images
        projects = load_projects()
        hero_data = []
        for hero_item in hero_images:
            project = next((p for p in projects if p.get("id") == hero_item.get("project_id")), None)
            if project:
                # Find the image in project
                image = next((img for img in project.get("images", []) if img.get("filename") == hero_item.get("image_filename")), None)
                if image:
                    hero_data.append({
                        "project_id": project["id"],
                        "image_url": url_for("serve_project_image", subpath=f"{project['id']}/{image['filename']}"),
                        "project_title": project.get("chu_dau_tu", ""),
                        "caption": hero_item.get("caption", "")
                    })
        return render_template("index.html", hero_images=hero_data)

    @app.route("/linh-vuc-kinh-doanh")
    def products():
        # Demo data; replace with real products later
        product_list = [
            {"name": "Giải pháp hạ tầng viễn thông", "desc": "Thi công, bảo trì, tối ưu hạ tầng.", "image": "images/sample-product-1.jpg"},
            {"name": "Năng lượng xanh", "desc": "Hệ thống điện mặt trời cho doanh nghiệp và hộ gia đình.", "image": "images/sample-product-2.jpg"},
            {"name": "Giải pháp tòa nhà thông minh", "desc": "Triển khai hệ thống IoT, M&E, an ninh.", "image": "images/sample-product-3.jpg"},
        ]
        return render_template("products.html", products=product_list)

    @app.route("/bao-gia")
    def quote():
        user = current_user()
        # If user is logged in, show internal quote template
        if user:
            hang_muc = load_hang_muc()
            gia_xay_tho = [g for g in load_gia_xay_tho() if g.get("active", True)]
            gia_hoan_thien = [g for g in load_gia_hoan_thien() if g.get("active", True)]
            vat_tu = load_vat_tu()
            # Sort by order
            hang_muc.sort(key=lambda x: x.get("order", 999))
            gia_xay_tho.sort(key=lambda x: x.get("order", 999))
            gia_hoan_thien.sort(key=lambda x: x.get("order", 999))
            return render_template("quote.html", hang_muc=hang_muc, gia_xay_tho=gia_xay_tho, gia_hoan_thien=gia_hoan_thien, vat_tu=vat_tu)
        # If not logged in, show public quote template
        else:
            administrative_units = load_administrative_units()
            return render_template("quote_public.html", administrative_units=administrative_units)

    @app.route("/hinh-anh")
    def gallery():
        projects = load_projects()
        # Sort by created_at descending (newest first)
        projects.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        # Get all unique progress options from all projects
        all_progress = set()
        for project in projects:
            for image in project.get("images", []):
                if image.get("progress"):
                    all_progress.add(image.get("progress"))
        # Also include progress options from settings
        progress_options = load_progress_options()
        all_progress.update(progress_options)
        all_progress = sorted(list(all_progress))
        return render_template("gallery.html", projects=projects, progress_options=all_progress)

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

    # -------- Construction Projects (Image Gallery) --------
    @app.route("/noi-bo/du-an-hinh-anh")
    @admin_required
    def projects_list():
        projects = load_projects()
        projects.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        return render_template("internal/projects_list.html", projects=projects)

    @app.route("/noi-bo/du-an-hinh-anh/tao", methods=["GET", "POST"])
    @admin_required
    def projects_create():
        if request.method == "POST":
            form = request.form
            project = {
                "id": uuid.uuid4().hex,
                "chu_dau_tu": form.get("chu_dau_tu", "").strip(),
                "quy_mo_du_an": form.get("quy_mo_du_an", "").strip(),
                "dia_chi_du_an": form.get("dia_chi_du_an", "").strip(),
                "ngay_khoi_cong": form.get("ngay_khoi_cong", "").strip(),
                "images": [],
                "created_at": _now_iso(),
                "created_by": session.get("username"),
            }
            if not project["chu_dau_tu"] or not project["dia_chi_du_an"]:
                flash("Chủ đầu tư và Địa chỉ dự án là bắt buộc.", "warning")
                return redirect(url_for("projects_create"))
            projects = load_projects()
            projects.append(project)
            save_projects(projects)
            flash("Đã tạo dự án hình ảnh.", "success")
            return redirect(url_for("projects_list"))
        return render_template("internal/projects_form.html", mode="create", project={})

    @app.route("/noi-bo/du-an-hinh-anh/sua/<project_id>", methods=["GET", "POST"])
    @admin_required
    def projects_edit(project_id):
        projects = load_projects()
        project = next((p for p in projects if p.get("id") == project_id), None)
        if not project:
            flash("Không tìm thấy dự án.", "danger")
            return redirect(url_for("projects_list"))
        if request.method == "POST":
            form = request.form
            project.update({
                "chu_dau_tu": form.get("chu_dau_tu", "").strip(),
                "quy_mo_du_an": form.get("quy_mo_du_an", "").strip(),
                "dia_chi_du_an": form.get("dia_chi_du_an", "").strip(),
                "ngay_khoi_cong": form.get("ngay_khoi_cong", "").strip(),
            })
            save_projects(projects)
            flash("Đã cập nhật dự án.", "success")
            return redirect(url_for("projects_list"))
        progress_options = load_progress_options()
        return render_template("internal/projects_form.html", mode="edit", project=project, progress_options=progress_options)

    @app.route("/noi-bo/du-an-hinh-anh/xoa/<project_id>", methods=["POST"])
    @admin_required
    def projects_delete(project_id):
        projects = load_projects()
        project = next((p for p in projects if p.get("id") == project_id), None)
        if not project:
            flash("Không tìm thấy dự án.", "danger")
            return redirect(url_for("projects_list"))
        # Delete image files
        uploads_root = Path(app.config['UPLOAD_FOLDER']).resolve()
        project_dir = uploads_root / "projects" / project_id
        if project_dir.exists():
            import shutil
            try:
                shutil.rmtree(project_dir)
            except Exception:
                pass
        # Remove from list
        projects = [p for p in projects if p.get("id") != project_id]
        save_projects(projects)
        flash("Đã xóa dự án.", "info")
        return redirect(url_for("projects_list"))

    @app.route("/noi-bo/du-an-hinh-anh/<project_id>/upload", methods=["POST"])
    @admin_required
    def projects_upload_images(project_id):
        projects = load_projects()
        project = next((p for p in projects if p.get("id") == project_id), None)
        if not project:
            flash("Không tìm thấy dự án.", "danger")
            return redirect(url_for("projects_list"))
        files = request.files.getlist("images")
        progress_options = load_progress_options()
        saved_any = False
        if files:
            uploads_root = Path(app.config['UPLOAD_FOLDER'])
            project_dir = uploads_root / "projects" / project_id
            project_dir.mkdir(parents=True, exist_ok=True)
            for f in files:
                if not f.filename:
                    continue
                filename = secure_filename(f.filename)
                # Generate unique filename to avoid conflicts
                file_id = uuid.uuid4().hex[:8]
                name_parts = filename.rsplit('.', 1)
                if len(name_parts) == 2:
                    unique_filename = f"{name_parts[0]}_{file_id}.{name_parts[1]}"
                else:
                    unique_filename = f"{filename}_{file_id}"
                dest = project_dir / unique_filename
                f.save(str(dest))
                # Get progress from form (same name for all images or per-image)
                progress = request.form.get("progress", progress_options[0] if progress_options else "")
                rel_path = f"projects/{project_id}/{unique_filename}"
                project.setdefault("images", []).append({
                    "id": uuid.uuid4().hex,
                    "filename": unique_filename,
                    "path": rel_path,
                    "progress": progress,
                    "uploaded_at": _now_iso(),
                    "uploader": session.get("username"),
                })
                saved_any = True
        if saved_any:
            save_projects(projects)
            flash("Đã tải lên hình ảnh.", "success")
        else:
            flash("Không có hình ảnh hợp lệ.", "warning")
        return redirect(url_for("projects_edit", project_id=project_id))

    @app.route("/noi-bo/du-an-hinh-anh/<project_id>/xoa-hinh/<image_id>", methods=["POST"])
    @admin_required
    def projects_delete_image(project_id, image_id):
        projects = load_projects()
        project = next((p for p in projects if p.get("id") == project_id), None)
        if not project:
            flash("Không tìm thấy dự án.", "danger")
            return redirect(url_for("projects_list"))
        images = project.get("images", [])
        image = next((img for img in images if img.get("id") == image_id), None)
        if image:
            # Delete file
            uploads_root = Path(app.config['UPLOAD_FOLDER']).resolve()
            file_path = uploads_root / image.get("path")
            if file_path.exists():
                try:
                    file_path.unlink()
                except Exception:
                    pass
            # Remove from list
            project["images"] = [img for img in images if img.get("id") != image_id]
            save_projects(projects)
            flash("Đã xóa hình ảnh.", "info")
        return redirect(url_for("projects_edit", project_id=project_id))

    @app.route("/noi-bo/du-an-hinh-anh/<project_id>/cap-nhat-tien-do/<image_id>", methods=["POST"])
    @admin_required
    def projects_update_progress(project_id, image_id):
        projects = load_projects()
        project = next((p for p in projects if p.get("id") == project_id), None)
        if not project:
            flash("Không tìm thấy dự án.", "danger")
            return redirect(url_for("projects_list"))
        images = project.get("images", [])
        image = next((img for img in images if img.get("id") == image_id), None)
        if image:
            new_progress = request.form.get("progress", "").strip()
            if new_progress:
                image["progress"] = new_progress
                save_projects(projects)
                flash("Đã cập nhật tiến độ.", "success")
        return redirect(url_for("projects_edit", project_id=project_id))

    # -------- Progress Options Management --------
    @app.route("/noi-bo/tien-do")
    @admin_required
    def progress_options_list():
        options = load_progress_options()
        return render_template("internal/progress_options.html", options=options)

    @app.route("/noi-bo/tien-do/them", methods=["POST"])
    @admin_required
    def progress_options_add():
        new_option = request.form.get("option", "").strip()
        if not new_option:
            flash("Vui lòng nhập tên tiến độ.", "warning")
            return redirect(url_for("progress_options_list"))
        options = load_progress_options()
        if new_option in options:
            flash("Tiến độ này đã tồn tại.", "warning")
            return redirect(url_for("progress_options_list"))
        options.append(new_option)
        save_progress_options(options)
        flash("Đã thêm tiến độ.", "success")
        return redirect(url_for("progress_options_list"))

    @app.route("/noi-bo/tien-do/xoa", methods=["POST"])
    @admin_required
    def progress_options_delete():
        option_to_delete = request.form.get("option", "").strip()
        if not option_to_delete:
            flash("Vui lòng chọn tiến độ cần xóa.", "warning")
            return redirect(url_for("progress_options_list"))
        options = load_progress_options()
        if option_to_delete not in options:
            flash("Không tìm thấy tiến độ.", "warning")
            return redirect(url_for("progress_options_list"))
        options.remove(option_to_delete)
        save_progress_options(options)
        flash("Đã xóa tiến độ.", "info")
        return redirect(url_for("progress_options_list"))

    @app.route("/uploads/projects/<path:subpath>")
    def serve_project_image(subpath):
        # Serve project images publicly (for gallery)
        uploads_root = Path(app.config['UPLOAD_FOLDER']).resolve()
        requested = (uploads_root / "projects" / subpath).resolve()
        if not str(requested).startswith(str(uploads_root / "projects")) or not requested.exists():
            return abort(404)
        return send_from_directory(directory=str(uploads_root / "projects"), path=subpath)

    # -------- Quote Management (Hạng mục & Giá xây thô) --------
    @app.route("/noi-bo/quan-ly-bao-gia")
    @admin_required
    def quote_management():
        hang_muc = load_hang_muc()
        gia_xay_tho = load_gia_xay_tho()
        gia_hoan_thien = load_gia_hoan_thien()
        vat_tu = load_vat_tu()
        hang_muc.sort(key=lambda x: x.get("order", 999))
        gia_xay_tho.sort(key=lambda x: x.get("order", 999))
        gia_hoan_thien.sort(key=lambda x: x.get("order", 999))
        return render_template("internal/quote_management.html", hang_muc=hang_muc, gia_xay_tho=gia_xay_tho, gia_hoan_thien=gia_hoan_thien, vat_tu=vat_tu)

    # Hạng mục management
    @app.route("/noi-bo/quan-ly-bao-gia/hang-muc/tao", methods=["POST"])
    @admin_required
    def hang_muc_create():
        name = request.form.get("name", "").strip()
        he_so = request.form.get("he_so", "").strip()
        try:
            he_so = float(he_so)
        except (ValueError, TypeError):
            flash("Hệ số phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not name:
            flash("Tên hạng mục không được để trống.", "warning")
            return redirect(url_for("quote_management"))
        hang_muc = load_hang_muc()
        max_order = max([h.get("order", 0) for h in hang_muc], default=0)
        new_item = {
            "id": uuid.uuid4().hex[:12],
            "name": name,
            "he_so": he_so,
            "order": max_order + 1,
        }
        hang_muc.append(new_item)
        save_hang_muc(hang_muc)
        flash("Đã thêm hạng mục.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/hang-muc/sua/<hang_muc_id>", methods=["POST"])
    @admin_required
    def hang_muc_edit(hang_muc_id):
        name = request.form.get("name", "").strip()
        he_so = request.form.get("he_so", "").strip()
        try:
            he_so = float(he_so)
        except (ValueError, TypeError):
            flash("Hệ số phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not name:
            flash("Tên hạng mục không được để trống.", "warning")
            return redirect(url_for("quote_management"))
        hang_muc = load_hang_muc()
        item = next((h for h in hang_muc if h.get("id") == hang_muc_id), None)
        if item:
            item["name"] = name
            item["he_so"] = he_so
            save_hang_muc(hang_muc)
            flash("Đã cập nhật hạng mục.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/hang-muc/xoa/<hang_muc_id>", methods=["POST"])
    @admin_required
    def hang_muc_delete(hang_muc_id):
        hang_muc = load_hang_muc()
        hang_muc = [h for h in hang_muc if h.get("id") != hang_muc_id]
        save_hang_muc(hang_muc)
        flash("Đã xóa hạng mục.", "info")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/hang-muc/sap-xep", methods=["POST"])
    @admin_required
    def hang_muc_reorder():
        order_data = request.json
        if not order_data:
            return {"success": False}, 400
        hang_muc = load_hang_muc()
        for item in hang_muc:
            if item.get("id") in order_data:
                item["order"] = order_data[item.get("id")]
        save_hang_muc(hang_muc)
        return {"success": True}

    # Giá xây thô management
    @app.route("/noi-bo/quan-ly-bao-gia/gia-xay-tho/tao", methods=["POST"])
    @admin_required
    def gia_xay_tho_create():
        gia = request.form.get("gia", "").strip()
        mo_ta = request.form.get("mo_ta", "").strip()
        try:
            gia = int(gia.replace(".", "").replace(",", ""))
        except (ValueError, TypeError):
            flash("Giá phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not mo_ta:
            mo_ta = f"{gia:,} VNĐ/m²".replace(",", ".")
        gia_list = load_gia_xay_tho()
        max_order = max([g.get("order", 0) for g in gia_list], default=0)
        new_item = {
            "id": uuid.uuid4().hex[:12],
            "gia": gia,
            "mo_ta": mo_ta,
            "active": True,
            "order": max_order + 1,
        }
        gia_list.append(new_item)
        save_gia_xay_tho(gia_list)
        flash("Đã thêm mức giá.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/gia-xay-tho/sua/<gia_id>", methods=["POST"])
    @admin_required
    def gia_xay_tho_edit(gia_id):
        gia = request.form.get("gia", "").strip()
        mo_ta = request.form.get("mo_ta", "").strip()
        active = request.form.get("active") == "on"
        try:
            gia = int(gia.replace(".", "").replace(",", ""))
        except (ValueError, TypeError):
            flash("Giá phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not mo_ta:
            mo_ta = f"{gia:,} VNĐ/m²".replace(",", ".")
        gia_list = load_gia_xay_tho()
        item = next((g for g in gia_list if g.get("id") == gia_id), None)
        if item:
            item["gia"] = gia
            item["mo_ta"] = mo_ta
            item["active"] = active
            save_gia_xay_tho(gia_list)
            flash("Đã cập nhật mức giá.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/gia-xay-tho/xoa/<gia_id>", methods=["POST"])
    @admin_required
    def gia_xay_tho_delete(gia_id):
        gia_list = load_gia_xay_tho()
        gia_list = [g for g in gia_list if g.get("id") != gia_id]
        save_gia_xay_tho(gia_list)
        flash("Đã xóa mức giá.", "info")
        return redirect(url_for("quote_management"))

    # Giá hoàn thiện management
    @app.route("/noi-bo/quan-ly-bao-gia/gia-hoan-thien/tao", methods=["POST"])
    @admin_required
    def gia_hoan_thien_create():
        gia = request.form.get("gia", "").strip()
        mo_ta = request.form.get("mo_ta", "").strip()
        try:
            gia = int(gia.replace(".", "").replace(",", ""))
        except (ValueError, TypeError):
            flash("Giá phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not mo_ta:
            mo_ta = f"{gia:,} VNĐ/m²".replace(",", ".")
        gia_list = load_gia_hoan_thien()
        max_order = max([g.get("order", 0) for g in gia_list], default=0)
        new_item = {
            "id": uuid.uuid4().hex[:12],
            "gia": gia,
            "mo_ta": mo_ta,
            "active": True,
            "order": max_order + 1,
        }
        gia_list.append(new_item)
        save_gia_hoan_thien(gia_list)
        flash("Đã thêm mức giá hoàn thiện.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/gia-hoan-thien/sua/<gia_id>", methods=["POST"])
    @admin_required
    def gia_hoan_thien_edit(gia_id):
        gia = request.form.get("gia", "").strip()
        mo_ta = request.form.get("mo_ta", "").strip()
        active = request.form.get("active") == "on"
        try:
            gia = int(gia.replace(".", "").replace(",", ""))
        except (ValueError, TypeError):
            flash("Giá phải là số hợp lệ.", "warning")
            return redirect(url_for("quote_management"))
        if not mo_ta:
            mo_ta = f"{gia:,} VNĐ/m²".replace(",", ".")
        gia_list = load_gia_hoan_thien()
        item = next((g for g in gia_list if g.get("id") == gia_id), None)
        if item:
            item["gia"] = gia
            item["mo_ta"] = mo_ta
            item["active"] = active
            save_gia_hoan_thien(gia_list)
            flash("Đã cập nhật mức giá hoàn thiện.", "success")
        return redirect(url_for("quote_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/gia-hoan-thien/xoa/<gia_id>", methods=["POST"])
    @admin_required
    def gia_hoan_thien_delete(gia_id):
        gia_list = load_gia_hoan_thien()
        gia_list = [g for g in gia_list if g.get("id") != gia_id]
        save_gia_hoan_thien(gia_list)
        flash("Đã xóa mức giá hoàn thiện.", "info")
        return redirect(url_for("quote_management"))

    # -------- Vật tư Management --------
    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu")
    @admin_required
    def vat_tu_management():
        vat_tu = load_vat_tu()
        # Ensure structure has xay_tho and hoan_thien
        if "xay_tho" not in vat_tu:
            vat_tu["xay_tho"] = {}
        if "hoan_thien" not in vat_tu:
            vat_tu["hoan_thien"] = {}
        # Convert dicts to lists of tuples for Jinja2 iteration
        vat_tu_xay_tho_list = list(vat_tu.get("xay_tho", {}).items())
        vat_tu_hoan_thien_list = list(vat_tu.get("hoan_thien", {}).items())
        gia_xay_tho = load_gia_xay_tho()
        gia_hoan_thien = load_gia_hoan_thien()
        return render_template("internal/vat_tu_management.html", 
                             vat_tu=vat_tu, 
                             vat_tu_xay_tho_list=vat_tu_xay_tho_list,
                             vat_tu_hoan_thien_list=vat_tu_hoan_thien_list,
                             gia_xay_tho=gia_xay_tho,
                             gia_hoan_thien=gia_hoan_thien)

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/tao-don-gia", methods=["POST"])
    @admin_required
    def vat_tu_create_gia():
        gia = request.form.get("gia", "").strip()
        mo_ta = request.form.get("mo_ta", "").strip()
        try:
            gia = int(gia.replace(".", "").replace(",", ""))
        except (ValueError, TypeError):
            flash("Giá phải là số hợp lệ.", "warning")
            return redirect(url_for("vat_tu_management"))
        if not mo_ta:
            mo_ta = f"{gia:,} VNĐ/m²".replace(",", ".")
        vat_tu = load_vat_tu()
        gia_key = str(gia)
        if gia_key in vat_tu:
            flash("Đơn giá này đã có dữ liệu vật tư.", "warning")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key] = {
            "gia": gia,
            "mo_ta": mo_ta,
            "categories": []
        }
        save_vat_tu(vat_tu)
        flash("Đã tạo đơn giá mới.", "success")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/xoa-don-gia/<gia_key>", methods=["POST"])
    @admin_required
    def vat_tu_delete_gia(gia_key):
        vat_tu = load_vat_tu()
        if gia_key in vat_tu:
            del vat_tu[gia_key]
            save_vat_tu(vat_tu)
            flash("Đã xóa đơn giá và dữ liệu vật tư.", "info")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/them-category", methods=["POST"])
    @admin_required
    def vat_tu_add_category(gia_key):
        name = request.form.get("name", "").strip()
        if not name:
            flash("Tên danh mục không được để trống.", "warning")
            return redirect(url_for("vat_tu_management"))
        vat_tu = load_vat_tu()
        if gia_key not in vat_tu:
            flash("Không tìm thấy đơn giá.", "danger")
            return redirect(url_for("vat_tu_management"))
        new_category = {
            "name": name,
            "items": []
        }
        vat_tu[gia_key]["categories"].append(new_category)
        save_vat_tu(vat_tu)
        flash("Đã thêm danh mục.", "success")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/sua-category/<int:cat_index>", methods=["POST"])
    @admin_required
    def vat_tu_edit_category(gia_key, cat_index):
        name = request.form.get("name", "").strip()
        if not name:
            flash("Tên danh mục không được để trống.", "warning")
            return redirect(url_for("vat_tu_management"))
        vat_tu = load_vat_tu()
        if gia_key not in vat_tu or cat_index >= len(vat_tu[gia_key]["categories"]):
            flash("Không tìm thấy danh mục.", "danger")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key]["categories"][cat_index]["name"] = name
        save_vat_tu(vat_tu)
        flash("Đã cập nhật danh mục.", "success")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/xoa-category/<int:cat_index>", methods=["POST"])
    @admin_required
    def vat_tu_delete_category(gia_key, cat_index):
        vat_tu = load_vat_tu()
        if gia_key not in vat_tu or cat_index >= len(vat_tu[gia_key]["categories"]):
            flash("Không tìm thấy danh mục.", "danger")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key]["categories"].pop(cat_index)
        save_vat_tu(vat_tu)
        flash("Đã xóa danh mục.", "info")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/them-item/<int:cat_index>", methods=["POST"])
    @admin_required
    def vat_tu_add_item(gia_key, cat_index):
        ten = request.form.get("ten", "").strip()
        chi_tiet = request.form.get("chi_tiet", "").strip()
        if not ten:
            flash("Tên vật tư không được để trống.", "warning")
            return redirect(url_for("vat_tu_management"))
        vat_tu = load_vat_tu()
        if gia_key not in vat_tu or cat_index >= len(vat_tu[gia_key]["categories"]):
            flash("Không tìm thấy danh mục.", "danger")
            return redirect(url_for("vat_tu_management"))
        new_item = {
            "ten": ten,
            "chi_tiet": chi_tiet
        }
        vat_tu[gia_key]["categories"][cat_index]["items"].append(new_item)
        save_vat_tu(vat_tu)
        flash("Đã thêm vật tư.", "success")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/sua-item/<int:cat_index>/<int:item_index>", methods=["POST"])
    @admin_required
    def vat_tu_edit_item(gia_key, cat_index, item_index):
        ten = request.form.get("ten", "").strip()
        chi_tiet = request.form.get("chi_tiet", "").strip()
        if not ten:
            flash("Tên vật tư không được để trống.", "warning")
            return redirect(url_for("vat_tu_management"))
        vat_tu = load_vat_tu()
        if (gia_key not in vat_tu or 
            cat_index >= len(vat_tu[gia_key]["categories"]) or
            item_index >= len(vat_tu[gia_key]["categories"][cat_index]["items"])):
            flash("Không tìm thấy vật tư.", "danger")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key]["categories"][cat_index]["items"][item_index]["ten"] = ten
        vat_tu[gia_key]["categories"][cat_index]["items"][item_index]["chi_tiet"] = chi_tiet
        save_vat_tu(vat_tu)
        flash("Đã cập nhật vật tư.", "success")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/xoa-item/<int:cat_index>/<int:item_index>", methods=["POST"])
    @admin_required
    def vat_tu_delete_item(gia_key, cat_index, item_index):
        vat_tu = load_vat_tu()
        if (gia_key not in vat_tu or 
            cat_index >= len(vat_tu[gia_key]["categories"]) or
            item_index >= len(vat_tu[gia_key]["categories"][cat_index]["items"])):
            flash("Không tìm thấy vật tư.", "danger")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key]["categories"][cat_index]["items"].pop(item_index)
        save_vat_tu(vat_tu)
        flash("Đã xóa vật tư.", "info")
        return redirect(url_for("vat_tu_management"))

    @app.route("/noi-bo/quan-ly-bao-gia/vat-tu/<gia_key>/cap-nhat-mo-ta", methods=["POST"])
    @admin_required
    def vat_tu_update_mo_ta(gia_key):
        mo_ta = request.form.get("mo_ta", "").strip()
        vat_tu = load_vat_tu()
        if gia_key not in vat_tu:
            flash("Không tìm thấy đơn giá.", "danger")
            return redirect(url_for("vat_tu_management"))
        vat_tu[gia_key]["mo_ta"] = mo_ta
        save_vat_tu(vat_tu)
        flash("Đã cập nhật mô tả.", "success")
        return redirect(url_for("vat_tu_management"))

    # -------- Hero Images Management --------
    @app.route("/noi-bo/quan-ly-hinh-anh-trang-chu")
    @admin_required
    def hero_images_management():
        projects = load_projects()
        hero_images = load_hero_images()
        # Enrich hero images with project info
        hero_with_info = []
        for hero_item in hero_images:
            project = next((p for p in projects if p.get("id") == hero_item.get("project_id")), None)
            if project:
                image = next((img for img in project.get("images", []) if img.get("filename") == hero_item.get("image_filename")), None)
                if image:
                    hero_with_info.append({
                        **hero_item,
                        "project_title": project.get("chu_dau_tu", ""),
                        "image_url": url_for("serve_project_image", subpath=f"{project['id']}/{image['filename']}"),
                        "caption": hero_item.get("caption", "")
                    })
        return render_template("internal/hero_images_management.html", projects=projects, hero_images=hero_with_info)

    @app.route("/noi-bo/quan-ly-hinh-anh-trang-chu/them", methods=["POST"])
    @admin_required
    def hero_images_add():
        project_id = request.form.get("project_id", "").strip()
        image_filename = request.form.get("image_filename", "").strip()
        caption = request.form.get("caption", "").strip()
        if not project_id or not image_filename:
            flash("Vui lòng chọn dự án và hình ảnh.", "warning")
            return redirect(url_for("hero_images_management"))
        hero_images = load_hero_images()
        # Check if already exists
        if any(h.get("project_id") == project_id and h.get("image_filename") == image_filename for h in hero_images):
            flash("Hình ảnh này đã được thêm vào trang chủ.", "warning")
            return redirect(url_for("hero_images_management"))
        hero_images.append({
            "project_id": project_id,
            "image_filename": image_filename,
            "caption": caption,
            "order": len(hero_images)
        })
        save_hero_images(hero_images)
        flash("Đã thêm hình ảnh vào trang chủ.", "success")
        return redirect(url_for("hero_images_management"))

    @app.route("/noi-bo/quan-ly-hinh-anh-trang-chu/xoa/<int:index>", methods=["POST"])
    @admin_required
    def hero_images_delete(index):
        hero_images = load_hero_images()
        if 0 <= index < len(hero_images):
            hero_images.pop(index)
            save_hero_images(hero_images)
            flash("Đã xóa hình ảnh khỏi trang chủ.", "info")
        return redirect(url_for("hero_images_management"))

    @app.route("/noi-bo/quan-ly-hinh-anh-trang-chu/sua-caption/<int:index>", methods=["POST"])
    @admin_required
    def hero_images_edit_caption(index):
        caption = request.form.get("caption", "").strip()
        hero_images = load_hero_images()
        if 0 <= index < len(hero_images):
            hero_images[index]["caption"] = caption
            save_hero_images(hero_images)
            flash("Đã cập nhật dòng chữ giới thiệu.", "success")
        return redirect(url_for("hero_images_management"))

    @app.route("/noi-bo/quan-ly-hinh-anh-trang-chu/sap-xep", methods=["POST"])
    @admin_required
    def hero_images_reorder():
        from flask import jsonify
        indices = request.json.get("indices", [])
        hero_images = load_hero_images()
        if len(indices) == len(hero_images):
            hero_images = [hero_images[i] for i in indices]
            save_hero_images(hero_images)
            return jsonify({"success": True})
        return jsonify({"success": False}), 400

    return app


# Expose a module-level WSGI variable for servers like gunicorn (app:app)
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


