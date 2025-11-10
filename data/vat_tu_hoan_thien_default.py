# Default data for hoan thien materials
# This file contains the default material data for finishing prices

def get_default_hoan_thien_data():
    """Returns default hoan thien material data"""
    return {
        "2150000": {
            "gia": 2150000,
            "mo_ta": "2.150.000 VNĐ/m²",
            "categories": [
                {
                    "name": "I. Gạch ốp lát",
                    "items": [
                        {"ten": "Gạch nền các tầng (CĐT tùy chọn mẫu gạch)", "chi_tiet": "Gạch 600x600 mờ (Thanh Long, Tasa, Taicera,…)\nĐơn giá ≤ 180,000/m²"},
                        {"ten": "Gạch nền sân thượng sân trước - sau", "chi_tiet": "Gạch 400x400 mờ (Viglacera, Prime, Bạch Mã, Tasa, Taicera, Casa…)\nĐơn giá ≤ 150,000/m²"},
                        {"ten": "Gạch nền WC", "chi_tiet": "(Viglacera, Prime, Bạch Mã, Tasa, Taicera, Casa…)\nGạch ốp theo mẫu\nĐơn giá ≤ 150,000/m²"},
                        {"ten": "Gạch ốp tường WC\nỐp cao < 2.7m", "chi_tiet": "Gạch ốp theo mẫu\nỐp cao < 2.7m\nKhông bao gồm len\nĐơn giá ≤ 150,000/m²"},
                        {"ten": "Keo chà ron", "chi_tiet": "Keo chà ron Weber\nCá sấu\nĐơn giá ≤ 30,000/m²"}
                    ]
                },
                {
                    "name": "II. Đá Granite",
                    "items": [
                        {"ten": "Đá trang trí mặt tiền, sân vườn", "chi_tiet": ""},
                        {"ten": "Đá Granite mặt tiền tầng trệt", "chi_tiet": ""},
                        {"ten": "Đá Granite tam cấp\n(Nếu có)", "chi_tiet": "Đá Trắng Suối Lau, Hồng Phan Rang, Tím Hoa Cà\nĐơn giá ≤ 650,000/m²"},
                        {"ten": "Đá Granite len cầu thang, ngạch cửa 100", "chi_tiet": "Đá Trắng Suối Lau, Hồng Phan Rang, Tím Hoa Cà\nĐơn giá ≤ 130,000/md"}
                    ]
                },
                {
                    "name": "III. Sơn nước",
                    "items": [
                        {"ten": "Sơn nước ngoài trời (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Maxilite, Expo, Bột trét cùng loại ngoài trời\nĐơn giá ≤ 55,000/m²"},
                        {"ten": "Sơn nước trong nhà (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Maxilite, Expo, Bột trét cùng loại trong nhà\nĐơn giá ≤ 50,000/m²"}
                    ]
                },
                {
                    "name": "IV. Cửa nhôm",
                    "items": [
                        {"ten": "Cửa đi các phòng", "chi_tiet": "Cửa nhôm Xingfa VN dày 1.2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 1,950,000/m²"},
                        {"ten": "Cửa đi WC", "chi_tiet": "Cửa nhôm Xingfa VN dày 1.2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 1,950,000/m²"},
                        {"ten": "Cửa mặt tiền chính\n(Mặt tiền, ban công, sân thượng, sân sau…)", "chi_tiet": "Cửa nhôm Xingfa VN dày 1.4mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,150,000/m²"}
                    ]
                },
                {
                    "name": "V. Hệ thống điện",
                    "items": [
                        {"ten": "Vỏ tủ điện Tổng và tủ điện Tầng (Loại 4 đường)\nTủ hộp nhựa cao cấp", "chi_tiet": "SINO"},
                        {"ten": "MCB, Công tắc, ổ cắm", "chi_tiet": "SINO\n(Mỗi phòng 4 công tắc,\n4 ổ cắm)"},
                        {"ten": "Đèn thắp sáng trong phòng, ngoài sân", "chi_tiet": "Đèn máng đôi 1.2m Philips 01 bóng, mỗi phòng 02 cái (hoặc tương đương 06 bóng đèn led tròn)\nĐơn giá ≤ 250,000/cái\nhoặc ≤ 130,000/đèn LED"},
                        {"ten": "Quạt hút WC", "chi_tiet": "Mỗi WC 01 cái\nĐơn giá ≤ 350,000/cái"},
                        {"ten": "Đèn WC", "chi_tiet": "Đèn mâm ốp trần,\nmỗi WC 01 cái.\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Đèn hắt trang trí trần thạch cao", "chi_tiet": "Mỗi phòng 04 bóng 1.2m (hoặc 8m đèn led dây)\nĐơn giá ≤ 150,000/cái (hoặc 80,000/m dây LED)"}
                    ]
                },
                {
                    "name": "VI. Thiết bị vệ sinh",
                    "items": [
                        {"ten": "Bàn cầu", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 2,800,000/cái"},
                        {"ten": "Lavabo + Bộ xả", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 1,100,000/cái"},
                        {"ten": "Vòi xả Lavabo", "chi_tiet": "Vòi lạnh\nViglacera, Caesar, Inax...\nĐơn giá ≤ 500,000/cái"},
                        {"ten": "Vòi xả sen WC (lạnh)", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 600,000/cái"},
                        {"ten": "Vòi xịt WC", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Vòi sân thượng, ban công, sân", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 150,000/cái"},
                        {"ten": "Các phụ kiện trong WC\n(Gương soi, móc treo đồ, kệ xà bông…)", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 600,000/cái"},
                        {"ten": "Phễu thu sàn", "chi_tiet": "Inox chống hôi\nĐơn giá ≤ 150,000/cái"},
                        {"ten": "Cầu chắn rác", "chi_tiet": "Inox\nĐơn giá ≤ 150,000/cái"}
                    ]
                },
                {
                    "name": "VII. Thiết bị nhà bếp",
                    "items": [
                        {"ten": "Chậu rửa chén", "chi_tiet": "Tân Á Đại Thành, Luxta, Javic...\nĐơn giá ≤ 1,000,000/cái"},
                        {"ten": "Vòi rửa chén", "chi_tiet": "Đại Thành, Luxta, Sơn Hà...\nĐơn giá ≤ 400,000/cái"}
                    ]
                },
                {
                    "name": "VIII. Hệ thống nước",
                    "items": [
                        {"ten": "Bồn nước Inox", "chi_tiet": "Tân Á Đại Thành 1000 lít\nĐơn giá ≤ 6,000,000/cái"},
                        {"ten": "Chân sắt nâng bồn nước", "chi_tiet": "Sắt V5\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Máy bơm nước", "chi_tiet": ""},
                        {"ten": "Hệ thống ống nước nóng", "chi_tiet": "Ống Vespo/PPR, Theo thiết kế bao gồm WC"}
                    ]
                },
                {
                    "name": "IX. Thạch cao và cửa cổng",
                    "items": [
                        {"ten": "Thạch cao trang trí", "chi_tiet": "Khung M29 Vĩnh Tường khung nổi, Tấm Gyproc Vĩnh Tường\nĐơn giá ≤ 150,000/m²"},
                        {"ten": "Cửa cổng", "chi_tiet": "Cửa sắt hộp dày 1mm sơn dầu, mẫu đơn giản\nĐơn giá ≤ 1,500,000/m²"},
                        {"ten": "Khung sắt mái lấy sáng cầu thang, lỗ thông tầng", "chi_tiet": "Sắt hộp 20x20x1.0mm\nSơn dầu\nĐơn giá ≤ 600,000/m²"},
                        {"ten": "Tấm lợp\nKính cường lực 8mm", "chi_tiet": "Đơn giá ≤ 750,000/m²"}
                    ]
                }
            ]
        },
        "2650000": {
            "gia": 2650000,
            "mo_ta": "2.650.000 VNĐ/m²",
            "categories": [
                {
                    "name": "I. Gạch ốp lát",
                    "items": [
                        {"ten": "Gạch nền các tầng (CĐT tùy chọn mẫu gạch)", "chi_tiet": "Gạch 600x600 mờ (Viglacera, Prime, Bạch Mã, Tasa, Taicera, Casa…)\nĐơn giá ≤ 260,000/m²"},
                        {"ten": "Gạch nền sân thượng sân trước - sau", "chi_tiet": "Gạch 400x400 mờ (Viglacera, Prime, Bạch Mã, Tasa, Taicera, Casa…)\nĐơn giá ≤ 170,000/m²"},
                        {"ten": "Gạch nền WC", "chi_tiet": "(Viglacera, Prime, Bạch Mã, Tasa, Taicera, Casa…)\nGạch ốp theo mẫu\nĐơn giá ≤ 170,000/m²"},
                        {"ten": "Gạch ốp tường WC\nỐp cao < 2.7m", "chi_tiet": "Gạch ốp theo mẫu\nỐp cao < 2.7m\nKhông bao gồm len\nĐơn giá ≤ 180,000/m²"},
                        {"ten": "Keo chà ron", "chi_tiet": "Keo chà ron Weber\nCá sấu\nĐơn giá ≤ 30,000/m²"}
                    ]
                },
                {
                    "name": "II. Đá Granite",
                    "items": [
                        {"ten": "Đá trang trí mặt tiền, sân vườn", "chi_tiet": ""},
                        {"ten": "Đá Granite mặt tiền tầng trệt", "chi_tiet": "Đá Trắng Suối Lau, Hồng Phan Rang, Tím Hoa Cà\nĐơn giá ≤ 950,000/m²"},
                        {"ten": "Đá Granite tam cấp\n(Nếu có)", "chi_tiet": "Đá Trắng Suối Lau, Hồng Phan Rang, Tím Hoa Cà\nĐơn giá ≤ 750,000/m²"},
                        {"ten": "Đá Granite len cầu thang, ngạch cửa 100", "chi_tiet": "Đá Trắng Suối Lau, Hồng Phan Rang, Tím Hoa Cà\nĐơn giá ≤ 130,000/md"}
                    ]
                },
                {
                    "name": "III. Sơn nước",
                    "items": [
                        {"ten": "Sơn nước ngoài trời (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Maxilite, Expo, Bột trét cùng loại ngoài trời\nĐơn giá ≤ 55,000/m²"},
                        {"ten": "Sơn nước trong nhà (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Maxilite, Expo, Bột trét cùng loại trong nhà\nĐơn giá ≤ 50,000/m²"}
                    ]
                },
                {
                    "name": "IV. Cửa nhôm",
                    "items": [
                        {"ten": "Cửa đi các phòng", "chi_tiet": "Cửa nhôm Xingfa VN dày 1.4mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,150,000/m²"},
                        {"ten": "Cửa đi WC", "chi_tiet": "Cửa nhôm Xingfa VN dày 1.4mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,150,000/m²"},
                        {"ten": "Cửa mặt tiền chính\n(Mặt tiền, ban công, sân thượng, sân sau…)", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,350,000/m²"}
                    ]
                },
                {
                    "name": "V. Hệ thống điện",
                    "items": [
                        {"ten": "Vỏ tủ điện Tổng và tủ điện Tầng (Loại 4 đường)\nTủ hộp nhựa cao cấp", "chi_tiet": "SINO"},
                        {"ten": "MCB, Công tắc, ổ cắm", "chi_tiet": "SINO\n(Mỗi phòng 4 công tắc,\n4 ổ cắm)"},
                        {"ten": "Đèn thắp sáng trong phòng, ngoài sân", "chi_tiet": "Đèn máng đôi 1.2m Philips 01 bóng, mỗi phòng 02 cái (hoặc tương đương 06 bóng đèn led tròn)\nĐơn giá ≤ 250,000/cái\nhoặc ≤ 130,000/đèn LED"},
                        {"ten": "Quạt hút WC", "chi_tiet": "Mỗi WC 01 cái\nĐơn giá ≤ 350,000/cái"},
                        {"ten": "Đèn WC", "chi_tiet": "Đèn mâm ốp trần,\nmỗi WC 01 cái.\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Đèn hắt trang trí trần thạch cao", "chi_tiet": "Mỗi phòng 04 bóng 1.2m (hoặc 8m đèn led dây)\nĐơn giá ≤ 150,000/cái (hoặc 80,000/m dây LED)"}
                    ]
                },
                {
                    "name": "VI. Thiết bị vệ sinh",
                    "items": [
                        {"ten": "Bàn cầu", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 3,000,000/cái"},
                        {"ten": "Lavabo + Bộ xả", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 1,100,000/cái"},
                        {"ten": "Vòi xả Lavabo", "chi_tiet": "Vòi lạnh\nViglacera, Caesar, Inax...\nĐơn giá ≤ 700,000/cái"},
                        {"ten": "Vòi xả sen WC (lạnh)", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 1,100,000/cái"},
                        {"ten": "Vòi xịt WC", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Vòi sân thượng, ban công, sân", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 150,000/cái"},
                        {"ten": "Các phụ kiện trong WC\n(Gương soi, móc treo đồ, kệ xà bông…)", "chi_tiet": "Viglacera, Caesar, Inax...\nĐơn giá ≤ 800,000/cái"},
                        {"ten": "Phễu thu sàn", "chi_tiet": "Inox chống hôi\nĐơn giá ≤ 150,000/cái"},
                        {"ten": "Cầu chắn rác", "chi_tiet": "Inox\nĐơn giá ≤ 150,000/cái"}
                    ]
                },
                {
                    "name": "VII. Thiết bị nhà bếp",
                    "items": [
                        {"ten": "Chậu rửa chén", "chi_tiet": "Tân Á Đại Thành, Luxta, Javic...\nĐơn giá ≤ 1,500,000/cái"},
                        {"ten": "Vòi rửa chén", "chi_tiet": "Đại Thành, Luxta, Sơn Hà...\nĐơn giá ≤ 500,000/cái"}
                    ]
                },
                {
                    "name": "VIII. Hệ thống nước",
                    "items": [
                        {"ten": "Bồn nước Inox", "chi_tiet": "Tân Á Đại Thành 1000 lít\nĐơn giá ≤ 6,000,000/cái"},
                        {"ten": "Chân sắt nâng bồn nước", "chi_tiet": "Sắt V5\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Máy bơm nước", "chi_tiet": "Panasonic - 200W\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Hệ thống ống nước nóng", "chi_tiet": "Ống Vespo/PPR, Theo thiết kế bao gồm WC"}
                    ]
                },
                {
                    "name": "IX. Thạch cao và cửa cổng",
                    "items": [
                        {"ten": "Thạch cao trang trí", "chi_tiet": "Khung M29 Vĩnh Tường, Tấm Gyproc Vĩnh Tường\nĐơn giá ≤ 175,000/m²"},
                        {"ten": "Cửa cổng", "chi_tiet": "Cửa sắt hộp dày 1mm sơn dầu, mẫu đơn giản\nĐơn giá ≤ 1,500,000/m²"},
                        {"ten": "Khung sắt mái lấy sáng cầu thang, lỗ thông tầng", "chi_tiet": "Sắt hộp 20x20x1.0mm\nSơn dầu\nĐơn giá ≤ 600,000/m²"},
                        {"ten": "Tấm lợp\nKính cường lực 8mm", "chi_tiet": "Đơn giá ≤ 750,000/m²"}
                    ]
                }
            ]
        },
        "3150000": {
            "gia": 3150000,
            "mo_ta": "3.150.000 VNĐ/m²",
            "categories": [
                {
                    "name": "I. Gạch ốp lát",
                    "items": [
                        {"ten": "Gạch nền các tầng (CĐT tùy chọn mẫu gạch)", "chi_tiet": "Gạch 800x800 bóng kính 2 da (Viglacera, Bạch Mã, Đồng Tâm…)\nĐơn giá ≤ 320,000/m²"},
                        {"ten": "Gạch nền sân thượng sân trước - sau", "chi_tiet": "Gạch 600x600 mờ (Viglacera, Bạch Mã, Đồng Tâm…)\nĐơn giá ≤ 220,000/m²"},
                        {"ten": "Gạch nền WC", "chi_tiet": "(Viglacera, Bạch Mã, Đồng Tâm…)\nGạch ốp theo mẫu\nĐơn giá ≤ 220,000/m²"},
                        {"ten": "Gạch ốp tường WC\nỐp cao < 2.7m", "chi_tiet": "Gạch ốp theo mẫu\nỐp cao < 2.7m\nKhông bao gồm len\nĐơn giá ≤ 220,000/m²"},
                        {"ten": "Keo chà ron", "chi_tiet": "Keo chà ron Weber\nCá sấu\nĐơn giá ≤ 30,000/m²"}
                    ]
                },
                {
                    "name": "II. Đá Granite",
                    "items": [
                        {"ten": "Đá trang trí mặt tiền, sân vườn", "chi_tiet": "CĐT chọn nhà cung cấp\nĐơn giá ≤ 500,000/m²"},
                        {"ten": "Đá Granite mặt tiền tầng trệt", "chi_tiet": "Đá Xanh Đen Campuchia, Trắng Ấn Độ, Hồng Gia Lai\nĐơn giá ≤ 1,200,000/m²"},
                        {"ten": "Đá Granite tam cấp\n(Nếu có)", "chi_tiet": "Đá Xanh Đen Campuchia, Trắng Ấn Độ, Hồng Gia Lai\nĐơn giá ≤ 950,000/m²"},
                        {"ten": "Đá Granite len cầu thang, ngạch cửa 100", "chi_tiet": "Đá Xanh Đen Campuchia, Trắng Ấn Độ, Hồng Gia Lai\nĐơn giá ≤ 170,000/md"}
                    ]
                },
                {
                    "name": "III. Sơn nước",
                    "items": [
                        {"ten": "Sơn nước ngoài trời (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Nippon, Dura\nBột trét cùng loại ngoài trời\nĐơn giá ≤ 65,000/m²"},
                        {"ten": "Sơn nước trong nhà (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Nippon, Dura\nBột trét cùng loại trong nhà\nĐơn giá ≤ 60,000/m²"}
                    ]
                },
                {
                    "name": "IV. Cửa nhôm",
                    "items": [
                        {"ten": "Cửa đi các phòng", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,550,000/m²"},
                        {"ten": "Cửa đi WC", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,550,000/m²"},
                        {"ten": "Cửa mặt tiền chính\n(Mặt tiền, ban công, sân thượng, sân sau…)", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,550,000/m²"}
                    ]
                },
                {
                    "name": "V. Hệ thống điện",
                    "items": [
                        {"ten": "Vỏ tủ điện Tổng và tủ điện Tầng (Loại 4 đường)\nTủ hộp nhựa cao cấp", "chi_tiet": "SINO"},
                        {"ten": "MCB, Công tắc, ổ cắm", "chi_tiet": "PANASONIC WIDE\n(Mỗi phòng 4 công tắc,\n4 ổ cắm)"},
                        {"ten": "Đèn thắp sáng trong phòng, ngoài sân", "chi_tiet": "Đèn máng đôi 1.2m Philips 01 bóng, mỗi phòng 04 cái (hoặc tương đương 08 bóng đèn led tròn)\nĐơn giá ≤ 250,000/cái\nhoặc ≤ 130,000/đèn LED"},
                        {"ten": "Quạt hút WC", "chi_tiet": "Mỗi WC 01 cái\nĐơn giá ≤ 350,000/cái"},
                        {"ten": "Đèn WC", "chi_tiet": "Đèn mâm ốp trần,\nmỗi WC 01 cái.\nĐơn giá ≤ 300,000/cái"},
                        {"ten": "Đèn hắt trang trí trần thạch cao", "chi_tiet": "Mỗi phòng 04 bóng LED (hoặc 10m đèn led dây)\nĐơn giá ≤ 200,000/cái (hoặc 80,000/m dây LED)"}
                    ]
                },
                {
                    "name": "VI. Thiết bị vệ sinh",
                    "items": [
                        {"ten": "Bàn cầu", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 4,000,000/cái"},
                        {"ten": "Lavabo + Bộ xả", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 1,600,000/cái"},
                        {"ten": "Vòi xả Lavabo", "chi_tiet": "Vòi nóng lạnh\nViglacera, Caesar, Inax, American...\nĐơn giá ≤ 1,400,000/cái"},
                        {"ten": "Vòi xả sen WC (lạnh)", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 2,100,000/cái"},
                        {"ten": "Vòi xịt WC", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 250,000/cái"},
                        {"ten": "Vòi sân thượng, ban công, sân", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Các phụ kiện trong WC\n(Gương soi, móc treo đồ, kệ xà bông…)", "chi_tiet": "Viglacera, Caesar, Inax, American...\nĐơn giá ≤ 1,000,000/cái"},
                        {"ten": "Phễu thu sàn", "chi_tiet": "Inox chống hôi\nĐơn giá ≤ 200,000/cái"},
                        {"ten": "Cầu chắn rác", "chi_tiet": "Inox\nĐơn giá ≤ 200,000/cái"}
                    ]
                },
                {
                    "name": "VII. Thiết bị nhà bếp",
                    "items": [
                        {"ten": "Chậu rửa chén", "chi_tiet": "Đại Thành, Luxta, Eurowin...\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Vòi rửa chén", "chi_tiet": "Đại Thành, Luxta, Eurowin...\nĐơn giá ≤ 800,000/cái"}
                    ]
                },
                {
                    "name": "VIII. Hệ thống nước",
                    "items": [
                        {"ten": "Bồn nước Inox", "chi_tiet": "Tân Á Đại Thành 1500 lít\nĐơn giá ≤ 8,500,000/cái"},
                        {"ten": "Chân sắt nâng bồn nước", "chi_tiet": "Sắt V5\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Máy bơm nước", "chi_tiet": "Panasonic - 200W\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Hệ thống ống nước nóng", "chi_tiet": "Ống Vesbo/PPR, Theo thiết kế bao gồm WC + Bếp"}
                    ]
                },
                {
                    "name": "IX. Thạch cao và cửa cổng",
                    "items": [
                        {"ten": "Thạch cao trang trí", "chi_tiet": "Khung TK4000 Vĩnh Tường, Tấm Gyproc dày 9mm\nĐơn giá ≤ 180,000/m²"},
                        {"ten": "Cửa cổng", "chi_tiet": "Cửa sắt hộp dày 1.2mm sơn dầu, theo mẫu\nĐơn giá ≤ 1,700,000/m²"},
                        {"ten": "Khung sắt mái lấy sáng cầu thang, lỗ thông tầng", "chi_tiet": "Sắt hộp 25x25x1.2mm\nSơn dầu\nĐơn giá ≤ 700,000/m²"},
                        {"ten": "Tấm lợp\nKính cường lực 8mm", "chi_tiet": "Đơn giá ≤ 750,000/m²"}
                    ]
                }
            ]
        },
        "3650000": {
            "gia": 3650000,
            "mo_ta": "3.650.000 VNĐ/m²",
            "categories": [
                {
                    "name": "I. Gạch ốp lát",
                    "items": [
                        {"ten": "Gạch nền các tầng (CĐT tùy chọn mẫu gạch)", "chi_tiet": "Gạch 800x800 bóng kính toàn phần (Vietceramic, Đồng Tâm, Trường Thịnh…)\nĐơn giá ≤ 360,000/m²"},
                        {"ten": "Gạch nền sân thượng sân trước - sau", "chi_tiet": "Gạch 600x600 mờ (Viglacera, Bạch Mã, Đồng Tâm…)\nĐơn giá ≤ 260,000/m²"},
                        {"ten": "Gạch nền WC", "chi_tiet": "(Vietceramic, Đồng Tâm, Trường Thịnh…)\nGạch ốp theo mẫu\nĐơn giá ≤ 280,000/m²"},
                        {"ten": "Gạch ốp tường WC\nỐp cao < 2.7m", "chi_tiet": "Gạch ốp theo mẫu\nỐp cao < 2.7m\nKhông bao gồm len\nĐơn giá ≤ 280,000/m²"},
                        {"ten": "Keo chà ron", "chi_tiet": "Keo chà ron Weber\nCá sấu\nĐơn giá ≤ 30,000/m²"}
                    ]
                },
                {
                    "name": "II. Đá Granite",
                    "items": [
                        {"ten": "Đá trang trí mặt tiền, sân vườn", "chi_tiet": "CĐT chọn nhà cung cấp\nĐơn giá ≤ 600,000/m²"},
                        {"ten": "Đá Granite mặt tiền tầng trệt", "chi_tiet": "Đá Marble, Kim Sa Trung, Nhân Tạo\nĐơn giá ≤ 1,500,000/m²"},
                        {"ten": "Đá Granite tam cấp\n(Nếu có)", "chi_tiet": "Đá Marble, Kim Sa Trung, Nhân Tạo\nĐơn giá ≤ 1,250,000/m²"},
                        {"ten": "Đá Granite len cầu thang, ngạch cửa 100", "chi_tiet": "Đá Marble, Kim Sa Trung, Nhân Tạo\nĐơn giá ≤ 210,000/md"}
                    ]
                },
                {
                    "name": "III. Sơn nước",
                    "items": [
                        {"ten": "Sơn nước ngoài trời (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Dulux, Jotun\nBột trét cùng loại ngoài trời\nĐơn giá ≤ 85,000/m²"},
                        {"ten": "Sơn nước trong nhà (02 lớp Matic, 01 lớp sơn lót, 02 lớp sơn phủ)\nPhụ kiện sơn nước: rulo, cọ, giấy nhám.", "chi_tiet": "Sơn Dulux, Jotun\nBột trét cùng loại trong nhà\nĐơn giá ≤ 80,000/m²"}
                    ]
                },
                {
                    "name": "IV. Cửa nhôm",
                    "items": [
                        {"ten": "Cửa đi các phòng", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,750,000/m²"},
                        {"ten": "Cửa đi WC", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,750,000/m²"},
                        {"ten": "Cửa mặt tiền chính\n(Mặt tiền, ban công, sân thượng, sân sau…)", "chi_tiet": "Cửa nhôm Xingfa VN dày 2mm màu xám ghi hoặc màu trắng, kính cường lực 8mm, phụ kiện KL\nĐơn giá ≤ 2,750,000/m²"}
                    ]
                },
                {
                    "name": "V. Hệ thống điện",
                    "items": [
                        {"ten": "Vỏ tủ điện Tổng và tủ điện Tầng (Loại 4 đường)\nTủ hộp nhựa cao cấp", "chi_tiet": "SINO"},
                        {"ten": "MCB, Công tắc, ổ cắm", "chi_tiet": "PANASONIC WIDE\n(Mỗi phòng 4 công tắc,\n4 ổ cắm)"},
                        {"ten": "Đèn thắp sáng trong phòng, ngoài sân", "chi_tiet": "Đèn máng đôi 1.2m Philips 01 bóng, mỗi phòng 06 cái (hoặc tương đương 10 bóng đèn led tròn)\nĐơn giá ≤ 250,000/cái\nhoặc ≤ 170,000/đèn LED"},
                        {"ten": "Quạt hút WC", "chi_tiet": "Mỗi WC 01 cái\nĐơn giá ≤ 800,000/cái"},
                        {"ten": "Đèn WC", "chi_tiet": "Đèn mâm ốp trần,\nmỗi WC 01 cái.\nĐơn giá ≤ 400,000/cái"},
                        {"ten": "Đèn hắt trang trí trần thạch cao", "chi_tiet": "Mỗi phòng 06 bóng LED (hoặc 15m đèn led dây)\nĐơn giá ≤ 200,000/cái (hoặc 80,000/m dây LED)"}
                    ]
                },
                {
                    "name": "VI. Thiết bị vệ sinh",
                    "items": [
                        {"ten": "Bàn cầu", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 6,000,000/cái"},
                        {"ten": "Lavabo + Bộ xả", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 3,000,000/cái"},
                        {"ten": "Vòi xả Lavabo", "chi_tiet": "Vòi nóng lạnh\nInax, Toto, American Standard...\nĐơn giá ≤ 2,500,000/cái"},
                        {"ten": "Vòi xả sen WC (lạnh)", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 3,000,000/cái"},
                        {"ten": "Vòi xịt WC", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 400,000/cái"},
                        {"ten": "Vòi sân thượng, ban công, sân", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 350,000/cái"},
                        {"ten": "Các phụ kiện trong WC\n(Gương soi, móc treo đồ, kệ xà bông…)", "chi_tiet": "Inax, Toto, American Standard...\nĐơn giá ≤ 1,500,000/cái"},
                        {"ten": "Phễu thu sàn", "chi_tiet": "Inox chống hôi\nĐơn giá ≤ 350,000/cái"},
                        {"ten": "Cầu chắn rác", "chi_tiet": "Inox\nĐơn giá ≤ 350,000/cái"}
                    ]
                },
                {
                    "name": "VII. Thiết bị nhà bếp",
                    "items": [
                        {"ten": "Chậu rửa chén", "chi_tiet": "Tân Á Đại Thành, Luxta, Javic...\nĐơn giá ≤ 2,500,000/cái"},
                        {"ten": "Vòi rửa chén", "chi_tiet": "Tân Á Đại Thành, Luxta, Javic...\nĐơn giá ≤ 1,000,000/cái"}
                    ]
                },
                {
                    "name": "VIII. Hệ thống nước",
                    "items": [
                        {"ten": "Bồn nước Inox", "chi_tiet": "Tân Á Đại Thành 2000 lít\nĐơn giá ≤ 10,000,000/cái"},
                        {"ten": "Chân sắt nâng bồn nước", "chi_tiet": "Sắt V5\nĐơn giá ≤ 2,000,000/cái"},
                        {"ten": "Máy bơm nước", "chi_tiet": "Panasonic - 250W\nĐơn giá ≤ 3,000,000/cái"},
                        {"ten": "Hệ thống ống nước nóng", "chi_tiet": "Ống Vesbo/PPR, Theo thiết kế bao gồm WC + Bếp"}
                    ]
                },
                {
                    "name": "IX. Thạch cao và cửa cổng",
                    "items": [
                        {"ten": "Thạch cao trang trí", "chi_tiet": "Khung Alpha 4000 Vĩnh Tường, Tấm Gyproc dày 9mm\nĐơn giá ≤ 190,000/m²"},
                        {"ten": "Cửa cổng", "chi_tiet": "Cửa sắt hộp dày 1.4mm sơn dầu, theo mẫu\nĐơn giá ≤ 2,000,000/m²"},
                        {"ten": "Khung sắt mái lấy sáng cầu thang, lỗ thông tầng", "chi_tiet": "Sắt hộp 25x25x1.2mm\nSơn dầu\nĐơn giá ≤ 700,000/m²"},
                        {"ten": "Tấm lợp\nKính cường lực 10mm", "chi_tiet": "Đơn giá ≤ 850,000/m²"}
                    ]
                }
            ]
        }
    }

