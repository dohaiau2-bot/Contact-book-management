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
            print("❌ SĐT không hợp lệ (Phải có 10 số, đầu 03, 05, 07, 08, 09).")
            continue
            
        if any(c['phone'] == phone for c in contacts):
            print(f"⚠️ Lỗi: Số điện thoại {phone} đã tồn tại!")
            if input("Nhập 'r' để thử lại, phím khác để thoát: ").lower() != 'r': return
        else: break 

    email = input("Nhập email: ").strip()
    
    # Tạo ID tự động tăng
    new_id_num = max([int(c['id']) for c in contacts]) + 1 if contacts else 1
    unique_id = f"{new_id_num:02d}"

    contacts.append({"id": unique_id, "name": name, "phone": phone, "email": email})
    luu_du_lieu(contacts)
    print(f"✅ Đã thêm thành công! ID: {unique_id}")

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

def xoa_lien_he(contacts):
    """Xóa liên hệ và cập nhật cả file .txt lẫn .json"""
    print("\n--- XÓA LIÊN HỆ ---")
    target_id = input("Nhập mã ID cần xóa (VD: 01): ").strip()
    
    found_contact = None
    for c in contacts:
        if c['id'] == target_id:
            found_contact = c
            break
    
    if found_contact:
        confirm = input(f"Xác nhận xóa '{found_contact['name']}'? (y/n): ").lower()
        if confirm == 'y':
            contacts.remove(found_contact)
            
            # Cập nhật file .txt
            luu_du_lieu(contacts)
            
            # Cập nhật file .json (nếu file đã tồn tại)
            if os.path.exists(JSON_FILE):
                xuat_json(contacts)
                
            print(f"✅ Đã xóa liên hệ {target_id} thành công khỏi các tệp lưu trữ.")
        else:
            print("Đã hủy thao tác xóa.")
    else:
        print(f"❌ Không tìm thấy liên hệ nào có mã ID: {target_id}")

def tim_kiem(contacts):
    query = input("\nNhập Tên hoặc ID cần tìm: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query == c['id']]
    hien_thi_danh_ba(results) if results else print("\nKhông tìm thấy kết quả.")

def sap_xep_danh_ba(contacts):
    contacts.sort(key=lambda x: x['name'].lower())
    print("\nĐã sắp xếp danh bạ theo tên.")
    hien_thi_danh_ba(contacts)

def thong_ke(contacts):
    print(f"\n--- THỐNG KÊ ---")
    print(f"Tổng số liên hệ hiện có: {len(contacts)}")

def xuat_json(contacts):
    """Xuất hoặc cập nhật dữ liệu ra JSON"""
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
        print(f"Đã cập nhật dữ liệu vào {JSON_FILE}")
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
    print("6. Xóa liên hệ (Cập nhật TXT & JSON)")
    print("7. Xuất file JSON (Nâng cao)")
    print("0. Thoát")
    print("===================================")

def main():
    contacts = tai_du_lieu()
    while True:
        hien_thi_menu()
        choice = input("Lựa chọn của bạn (0-7): ")
        if choice == '1': them_lien_he(contacts)
        elif choice == '2': hien_thi_danh_ba(contacts)
        elif choice == '3': tim_kiem(contacts)
        elif choice == '4': sap_xep_danh_ba(contacts)
        elif choice == '5': thong_ke(contacts)
        elif choice == '6': xoa_lien_he(contacts)
        elif choice == '7': xuat_json(contacts)
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()