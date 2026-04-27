import json
import os
import re

# Tên tệp lưu trữ dữ liệu
TXT_FILE = "contacts.txt"
JSON_FILE = "contacts.json"

# --- CHỨC NĂNG HỆ THỐNG ---

def tai_du_lieu():
    """Tải dữ liệu từ file TXT"""
    contacts = []
    if not os.path.exists(TXT_FILE):
        return contacts
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = [p.strip() for p in line.strip().split("|")]
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
    """Ghi dữ liệu vào file TXT"""
    try:
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(f"{c['id']}|{c['name']}|{c['phone']}|{c['email']}\n")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def kiem_tra_sdt(phone):
    pattern = r"^(0[3|5|7|8|9])[0-9]{8}$"
    return re.match(pattern, phone)

# --- CHỨC NĂNG QUẢN LÝ (CRUD) ---

def them_lien_he(contacts):
    print("\n--- THÊM LIÊN HỆ MỚI ---")
    name = input("Nhập tên: ").strip()
    while not name:
        name = input("Tên không được để trống. Nhập lại: ").strip()
    
    while True:
        phone = input("Nhập số điện thoại (10 số): ").strip()
        if not kiem_tra_sdt(phone):
            print("❌ SĐT không hợp lệ.")
            continue
        if any(c['phone'] == phone for c in contacts):
            print(f"⚠️ Số điện thoại {phone} đã tồn tại!")
            if input("Nhập 'r' để thử lại hoặc phím bất kỳ để hủy: ").lower() != 'r': return
        else: break 

    email = input("Nhập email: ").strip()

    # Thuật toán tìm ID trống nhỏ nhất
    existing_ids = {int(c['id']) for c in contacts}
    new_id_num = 1
    while new_id_num in existing_ids:
        new_id_num += 1
    unique_id = f"{new_id_num:02d}"

    contacts.append({"id": unique_id, "name": name, "phone": phone, "email": email})
    luu_du_lieu(contacts)
    print(f"✅ Đã thêm thành công! ID: {unique_id}")

def hien_thi_danh_ba(contacts_list):
    if not contacts_list:
        print("\nDanh sách trống.")
        return
    print("\n" + "="*80)
    print(f"{'ID':<5} | {'Họ và Tên':<25} | {'Số điện thoại':<15} | {'Email'}")
    print("-" * 80)
    for c in contacts_list:
        print(f"{c['id']:<5} | {c['name']:<25} | {c['phone']:<15} | {c['email']}")
    print("="*80)

# --- [ADVANCED] TÌM KIẾM & LỌC NÂNG CAO (PHẦN 8 TRONG RUBRIC) ---

def tim_kiem_va_loc(contacts):
    """
    Triển khai Tìm kiếm chuỗi con (substring) 
    VÀ Lọc theo điều kiện (filter by conditions)
    """
    print("\n--- TÌM KIẾM & LỌC NÂNG CAO ---")
    print("1. Tìm kiếm theo Tên (Khớp một phần - Substring)")
    print("2. Lọc theo nhà cung cấp Email (VD: gmail.com, yahoo.com)")
    print("3. Lọc theo đầu số điện thoại (VD: 035, 090)")
    print("0. Quay lại")
    
    choice = input("Lựa chọn kiểu tìm lọc: ")
    results = []

    if choice == '1':
        query = input("Nhập tên hoặc một phần tên cần tìm: ").strip().lower()
        # Logic: Search by substrings
        results = [c for c in contacts if query in c['name'].lower()]
        
    elif choice == '2':
        domain = input("Nhập tên miền email cần lọc (VD: gmail): ").strip().lower()
        # Logic: Filter records by conditions (Email)
        results = [c for c in contacts if domain in c['email'].lower()]
        
    elif choice == '3':
        prefix = input("Nhập đầu số điện thoại cần lọc: ").strip()
        # Logic: Filter records by conditions (Phone prefix)
        results = [c for c in contacts if c['phone'].startswith(prefix)]
        
    elif choice == '0':
        return
    else:
        print("Lựa chọn không hợp lệ.")
        return

    if results:
        print(f"\nKết quả tìm kiếm/lọc (Tìm thấy {len(results)} bản ghi):")
        hien_thi_danh_ba(results)
    else:
        print("\n❌ Không tìm thấy kết quả nào phù hợp với yêu cầu.")

# --- CÁC CHỨC NĂNG KHÁC ---

def vietnamese_sort_key(full_name):
    if not full_name: return ""
    dict_map = {
        'a': 'a0', 'à': 'a1', 'ả': 'a2', 'ã': 'a3', 'á': 'a4', 'ạ': 'a5',
        'ă': 'a6', 'ằ': 'a7', 'ẳ': 'a8', 'ẵ': 'a9', 'ắ': 'a10', 'ặ': 'a11',
        'â': 'a12', 'ầ': 'a13', 'ẩ': 'a14', 'ẫ': 'a15', 'ấ': 'a16', 'ậ': 'a17',
        'đ': 'd1', 'd': 'd0', 'e': 'e0', 'è': 'e1', 'ẻ': 'e2', 'ẽ': 'e3', 'é': 'e4', 'ẹ': 'e5',
        'ê': 'e6', 'ề': 'e7', 'ể': 'e8', 'ễ': 'e9', 'ế': 'e10', 'ệ': 'e11',
    }
    def convert_word(word):
        return "".join([dict_map.get(char, char) for char in word.lower()])

    parts = full_name.strip().split()
    if not parts: return ""
    last_name = convert_word(parts[-1])
    full_normalized = convert_word(" ".join(parts))
    return (last_name, full_normalized)

def sap_xep_danh_ba(contacts):
    if not contacts: return
    contacts.sort(key=lambda x: vietnamese_sort_key(x['name']))
    print("\n✅ Đã sắp xếp danh bạ theo Tên (A-Z).")
    hien_thi_danh_ba(contacts)

def thong_ke(contacts):
    print(f"\n--- THỐNG KÊ ---")
    print(f"Tổng số liên hệ hiện có: {len(contacts)}")
    
    if not contacts:
        return

    print("\nChi tiết phân nhóm theo tên miền Email:")
    email_groups = {}
    
    for c in contacts:
        email = c.get('email', '').strip()
        if "@" in email:
            # Tách lấy phần tên miền sau chữ @ (VD: gmail.com)
            domain = email.split('@')[1].lower()
        else:
            domain = "Không có/Không hợp lệ"
            
        # Đếm số lượng cho từng nhóm
        if domain in email_groups:
            email_groups[domain] += 1
        else:
            email_groups[domain] = 1

    # In kết quả thống kê theo nhóm
    for domain, count in email_groups.items():
        print(f" - {domain}: {count} liên hệ")
    print("-" * 20)

def xoa_lien_he(contacts):
    raw_id = input("\nNhập mã ID cần xóa: ").strip()
    try:
        target_id = f"{int(raw_id):02d}"
    except:
        target_id = raw_id
    
    initial_count = len(contacts)
    contacts[:] = [c for c in contacts if c['id'] != target_id]
    
    if len(contacts) < initial_count:
        luu_du_lieu(contacts)
        print(f"✅ Đã xóa ID {target_id}")
    else:
        print(f"❌ Không tìm thấy ID: {target_id}")

def xuat_json(contacts):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Lỗi: {e}")

# --- MENU HỆ THỐNG ---

def hien_thi_menu():
    print("\n" + "="*15 + " QUẢN LÝ DANH BẠ " + "="*15)
    print("1. Thêm liên hệ mới")
    print("2. Hiển thị danh bạ")
    print("3. Tìm kiếm & Lọc nâng cao (Advanced)")
    print("4. Sắp xếp danh bạ (A-Z)")
    print("5. Thống kê số lượng")
    print("6. Xóa liên hệ")
    print("7. Xuất file JSON")
    print("0. Thoát")
    print("="*47)

def main():
    contacts = tai_du_lieu()
    while True:
        hien_thi_menu()
        choice = input("Lựa chọn (0-7): ")
        if choice == '1': them_lien_he(contacts)
        elif choice == '2': hien_thi_danh_ba(contacts)
        elif choice == '3': tim_kiem_va_loc(contacts)
        elif choice == '4': sap_xep_danh_ba(contacts)
        elif choice == '5': thong_ke(contacts)
        elif choice == '6': xoa_lien_he(contacts)
        elif choice == '7': 
            xuat_json(contacts)
            print(f"✅ Đã xuất ra file {JSON_FILE}")
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()