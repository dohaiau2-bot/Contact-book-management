import json
import os
import re

# Tên tệp lưu trữ dữ liệu
TXT_FILE = "contacts.txt"
JSON_FILE = "contacts.json"

# --- CHỨC NĂNG HỆ THỐNG ---

def tai_du_lieu():
    """Tải dữ liệu từ tệp .txt"""
    contacts = []
    if not os.path.exists(TXT_FILE):
        return contacts
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    contacts.append({
                        "id": parts[0], 
                        "name": parts[1], 
                        "phone": parts[2], 
                        "email": parts[3]
                    })
    except Exception as e:
        print(f"Lỗi khi tải file: {e}")
    return contacts

def luu_du_lieu(contacts):
    """Lưu dữ liệu vào tệp .txt"""
    try:
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(f"{c['id']}|{c['name']}|{c['phone']}|{c['email']}\n")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def kiem_tra_sdt(phone):
    """Kiểm tra định dạng số điện thoại Việt Nam"""
    pattern = r"^(0[3|5|7|8|9])[0-9]{8}$"
    return re.match(pattern, phone)

def them_lien_he(contacts):
    """Thêm liên hệ mới: Tự động tạo ID tuần tự (01, 02, 03...)"""
    print("\n--- THÊM LIÊN HỆ MỚI ---")
    
    name = input("Nhập tên: ").strip()
    while not name:
        name = input("Tên không được để trống. Nhập lại: ").strip()
    
    while True:
        phone = input("Nhập số điện thoại (10 số): ").strip()
        
        if not kiem_tra_sdt(phone):
            print("❌ SĐT không hợp lệ (Phải có 10 số, bắt đầu bằng 03, 05, 07, 08, 09).")
            continue
            
        trung_lap = any(c['phone'] == phone for c in contacts)
        if trung_lap:
            print(f"⚠️ Lỗi: Số điện thoại {phone} đã tồn tại trong danh bạ!")
            lua_chon = input("Nhập 'r' để thử lại, hoặc phím bất kỳ để thoát: ").lower()
            if lua_chon != 'r':
                return 
        else:
            break 

    email = input("Nhập email: ").strip()
    
    # --- THUẬT TOÁN TẠO ID TỰ ĐỘNG TĂNG ---
    if not contacts:
        # Nếu danh bạ trống, bắt đầu từ 1
        new_id_num = 1
    else:
        # Tìm ID lớn nhất hiện tại (phải ép kiểu int để so sánh toán học)
        max_id = max(int(c['id']) for c in contacts)
        new_id_num = max_id + 1
        
    # Format số nguyên thành chuỗi có 2 chữ số (VD: 1 -> "01", 12 -> "12")
    unique_id = f"{new_id_num:02d}"
    # ----------------------------------------

    contacts.append({"id": unique_id, "name": name, "phone": phone, "email": email})
    luu_du_lieu(contacts)
    print(f"✅ Đã thêm thành công! Mã ID của {name} là: {unique_id}")

def hien_thi_danh_ba(contacts):
    if not contacts:
        print("\nDanh bạ trống.")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} | {'Họ và Tên':<20} | {'Số điện thoại':<15} | {'Email'}")
    print("-" * 70)
    for c in contacts:
        print(f"{c['id']:<5} | {c['name']:<20} | {c['phone']:<15} | {c['email']}")
    print("="*70)

def tim_kiem(contacts):
    query = input("\nNhập Tên hoặc ID cần tìm (VD: 01): ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query == c['id']]
    
    if results:
        print(f"\nTìm thấy {len(results)} kết quả:")
        hien_thi_danh_ba(results)
    else:
        print("\nKhông tìm thấy kết quả phù hợp.")

def sap_xep_danh_ba(contacts):
    contacts.sort(key=lambda x: x['name'].lower())
    print("\nĐã sắp xếp danh bạ theo tên.")
    hien_thi_danh_ba(contacts)

def thong_ke(contacts):
    total = len(contacts)
    print(f"\n--- THỐNG KÊ ---")
    print(f"Tổng số liên hệ hiện có: {total}")

def xuat_json(contacts):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
        print(f"Đã xuất dữ liệu thành công ra {JSON_FILE}")
    except Exception as e:
        print(f"Lỗi xuất JSON: {e}")

# --- MENU CHÍNH ---

def hien_thi_menu():
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
        
        if choice == '1': them_lien_he(contacts)
        elif choice == '2': hien_thi_danh_ba(contacts)
        elif choice == '3': tim_kiem(contacts)
        elif choice == '4': sap_xep_danh_ba(contacts)
        elif choice == '5': thong_ke(contacts)
        elif choice == '6': xuat_json(contacts)
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()