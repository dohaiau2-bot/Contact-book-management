import json
import os
import re

# Tên tệp lưu trữ dữ liệu
TXT_FILE = "contacts.txt"
JSON_FILE = "contacts.json"

# --- CHỨC NĂNG HỆ THỐNG ---

def tai_du_lieu():
    """Tải dữ liệu từ tệp .txt khi khởi động [cite: 34, 77]"""
    contacts = []
    if not os.path.exists(TXT_FILE):
        return contacts
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    except Exception as e:
        print(f"Lỗi khi tải file: {e}")
    return contacts

def luu_du_lieu(contacts):
    """Lưu dữ liệu vào tệp .txt [cite: 34, 77]"""
    try:
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(f"{c['name']}|{c['phone']}|{c['email']}\n")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def kiem_tra_sdt(phone):
    """Kiểm tra định dạng số điện thoại Việt Nam (10 số, bắt đầu bằng 0)"""
    # Regex cho SĐT VN: Bắt đầu bằng 0, theo sau là 9 chữ số
    pattern = r"^(0[3|5|7|8|9])[0-9]{8}$"
    return re.match(pattern, phone)

def them_lien_he(contacts):
    """Thêm liên hệ mới với xác thực SĐT chuẩn VN"""
    print("\n--- THÊM LIÊN HỆ MỚI ---")
    name = input("Nhập tên: ").strip()
    while not name:
        name = input("Tên không được để trống. Nhập lại: ").strip()
    
    phone = input("Nhập số điện thoại (VD: 0912345678): ").strip()
    while not kiem_tra_sdt(phone):
        phone = input("SĐT không hợp lệ (Phải có 10 số, bắt đầu bằng 03, 05, 07, 08, 09). Nhập lại: ").strip()
        
    email = input("Nhập email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    luu_du_lieu(contacts)
    print("Thêm thành công!")
    
def hien_thi_danh_ba(contacts):
    """Hiển thị danh sách dưới dạng bảng [cite: 38, 74]"""
    if not contacts:
        print("\nDanh bạ trống.")
        return
    
    print("\n" + "="*50)
    print(f"{'STT':<5} | {'Họ và Tên':<20} | {'Số điện thoại':<15} | {'Email'}")
    print("-" * 50)
    for i, c in enumerate(contacts, 1):
        print(f"{i:<5} | {c['name']:<20} | {c['phone']:<15} | {c['email']}")
    print("="*50)

def tim_kiem(contacts):
    """Tìm kiếm chính xác hoặc tìm kiếm chuỗi con [cite: 40, 52]"""
    query = input("\nNhập tên cần tìm: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower()]
    
    if results:
        print(f"\nTìm thấy {len(results)} kết quả:")
        hien_thi_danh_ba(results)
    else:
        print("\nKhông tìm thấy kết quả phù hợp.")

def sap_xep_danh_ba(contacts):
    """Sắp xếp theo tên từ A-Z [cite: 42, 74]"""
    contacts.sort(key=lambda x: x['name'].lower())
    print("\nĐã sắp xếp danh bạ theo tên.")
    hien_thi_danh_ba(contacts)

def thong_ke(contacts):
    """Thực hiện các phép toán thống kê cơ bản [cite: 44, 77]"""
    total = len(contacts)
    print(f"\n--- THỐNG KÊ ---")
    print(f"Tổng số liên hệ hiện có: {total}")

def xuat_json(contacts):
    """Chức năng nâng cao: Xuất dữ liệu ra JSON [cite: 56, 77]"""
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
        print(f"Đã xuất dữ liệu thành công ra {JSON_FILE}")
    except Exception as e:
        print(f"Lỗi xuất JSON: {e}")

# --- MENU CHÍNH ---

def hien_thi_menu():
    """Hiển thị menu tương tác [cite: 31, 74]"""
    print("\n===== QUẢN LÝ DANH BẠ LIÊN HỆ =====")
    print("1. Thêm liên hệ mới")
    print("2. Hiển thị danh bạ")
    print("3. Tìm kiếm liên hệ")
    print("4. Sắp xếp danh bạ (A-Z)")
    print("5. Thống kê số lượng")
    print("6. Xuất file JSON (Nâng cao)")
    print("0. Thoát")
    print("===================================")

def main():
    contacts = tai_du_lieu()
    while True:
        hien_thi_menu()
        choice = input("Lựa chọn của bạn (0-6): ")
        
        if choice == '1':
            them_lien_he(contacts)
        elif choice == '2':
            hien_thi_danh_ba(contacts)
        elif choice == '3':
            tim_kiem(contacts)
        elif choice == '4':
            sap_xep_danh_ba(contacts)
        elif choice == '5':
            thong_ke(contacts)
        elif choice == '6':
            xuat_json(contacts)
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()