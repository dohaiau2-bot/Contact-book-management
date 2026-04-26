import json
import os
import re

# Tên tệp lưu trữ dữ liệu
TXT_FILE = "contacts.txt"
JSON_FILE = "contacts.json"

# --- CHỨC NĂNG HỆ THỐNG ---

def tai_du_lieu():
    """Tải dữ liệu và làm sạch khoảng trắng thừa"""
    contacts = []
    if not os.path.exists(TXT_FILE):
        return contacts
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                # Dùng list comprehension để strip từng phần tử sau khi split
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
    """Ghi đè hoàn toàn danh sách mới vào file .txt"""
    try:
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(f"{c['id']}|{c['name']}|{c['phone']}|{c['email']}\n")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def kiem_tra_sdt(phone):
    pattern = r"^(0[3|5|7|8|9])[0-9]{8}$"
    return re.match(pattern, phone)

def kiem_tra_email_don_gian(email):
    if not email: return True #
    return "@" in email and "." in email 

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
            if input("Nhập 'r' để thử lại: ").lower() != 'r': return
        else: break 

    email = input("Nhập email: ").strip()

    # --- THUẬT TOÁN TÌM ID TRỐNG NHỎ NHẤT ---
    existing_ids = {int(c['id']) for c in contacts}
    new_id_num = 1
    while new_id_num in existing_ids:
        new_id_num += 1
    unique_id = f"{new_id_num:02d}"
    # ---------------------------------------

    contacts.append({"id": unique_id, "name": name, "phone": phone, "email": email})
    luu_du_lieu(contacts)
    if os.path.exists(JSON_FILE): xuat_json(contacts)
    print(f"✅ Đã thêm thành công! ID mới cấp: {unique_id}")

def xoa_lien_he(contacts):
    """Xóa triệt để mọi bản ghi trùng ID và đồng bộ tất cả tệp tin"""
    print("\n--- XÓA LIÊN HỆ ---")
    raw_id = input("Nhập mã ID cần xóa (VD: 01 hoặc 1): ").strip()
    
    # Chuẩn hóa ID người dùng nhập: "1" -> "01" để khớp với dữ liệu
    try:
        target_id = f"{int(raw_id):02d}"
    except ValueError:
        target_id = raw_id # Nếu nhập chữ thì giữ nguyên để báo lỗi sau

    # Tìm danh sách các liên hệ khớp ID (để báo cáo người dùng)
    to_delete = [c for c in contacts if c['id'] == target_id]
    
    if to_delete:
        print(f"Tìm thấy {len(to_delete)} liên hệ có ID {target_id}:")
        for item in to_delete:
            print(f" - {item['name']} ({item['phone']})")
            
        confirm = input(f"Xác nhận xóa VĨNH VIỄN? (y/n): ").lower()
        if confirm == 'y':
            # Kỹ thuật xóa triệt để: Lọc bỏ tất cả những gì có ID này
            contacts[:] = [c for c in contacts if c['id'] != target_id]
            
            # Cập nhật tất cả các nguồn lưu trữ
            luu_du_lieu(contacts)
            xuat_json(contacts) # Ép cập nhật JSON để đồng bộ hoàn toàn
                
            print(f"✅ Đã xóa sạch ID {target_id} khỏi hệ thống (TXT & JSON).")
        else:
            print("Hủy thao tác xóa.")
    else:
        print(f"❌ Không tìm thấy liên hệ nào có mã ID: {target_id}")

def sua_lien_he(contacts):
    print("\n--- SỬA ĐỔI LIÊN HỆ ---")
    raw_id = input("Nhập mã ID cần sửa: ").strip()
    try:
        target_id = f"{int(raw_id):02d}"
    except:
        target_id = raw_id

    contact = next((c for c in contacts if c['id'] == target_id), None)
    if not contact:
        print(f"❌ Không tìm thấy ID: {target_id}")
        return

    print(f"Đang sửa: {contact['name']}")
    new_name = input(f"Tên mới [{contact['name']}]: ").strip()
    if new_name: contact['name'] = new_name

    while True:
        new_phone = input(f"SĐT mới [{contact['phone']}]: ").strip()
        if not new_phone: break
        if not kiem_tra_sdt(new_phone): continue
        if any(c['phone'] == new_phone and c['id'] != target_id for c in contacts):
            print("⚠️ Số này đã tồn tại ở liên hệ khác!")
            continue
        contact['phone'] = new_phone
        break

    new_email = input(f"Email mới [{contact['email']}]: ").strip()
    if new_email: contact['email'] = new_email

    luu_du_lieu(contacts)
    xuat_json(contacts)
    print(f"✅ Cập nhật thành công ID {target_id}")

def hien_thi_danh_ba(contacts):
    if not contacts:
        print("\nDanh bạ trống.")
        return
    print("\n" + "="*75)
    print(f"{'ID':<5} | {'Họ và Tên':<20} | {'Số điện thoại':<15} | {'Email'}")
    print("-" * 75)
    for c in contacts:
        print(f"{c['id']:<5} | {c['name']:<20} | {c['phone']:<15} | {c['email']}")
    print("="*75)

def tim_kiem(contacts):
    query = input("\nNhập Tên hoặc ID cần tìm: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query == c['id']]
    hien_thi_danh_ba(results) if results else print("\nKhông tìm thấy kết quả.")

def vietnamese_sort_key(full_name):
    """
    Hàm này chuẩn hóa tên để máy tính sắp xếp đúng chuẩn Tiếng Việt.
    Nó sẽ lấy Tên cuối cùng để so sánh trước.
    """
    if not full_name: return ""
    
    # Bảng quy đổi ký tự Tiếng Việt sang một chuỗi có thể sắp xếp theo thứ tự Unicode
    # Chúng ta thay các chữ có dấu thành các ký tự đặc biệt để 'ă' luôn sau 'a', 'â' luôn sau 'ă', v.v.
    dict_map = {
        'a': 'a0', 'à': 'a1', 'ả': 'a2', 'ã': 'a3', 'á': 'a4', 'ạ': 'a5',
        'ă': 'a6', 'ằ': 'a7', 'ẳ': 'a8', 'ẵ': 'a9', 'ắ': 'a10', 'ặ': 'a11',
        'â': 'a12', 'ầ': 'a13', 'ẩ': 'a14', 'ẫ': 'a15', 'ấ': 'a16', 'ậ': 'a17',
        'đ': 'd1', 'd': 'd0',
        'e': 'e0', 'è': 'e1', 'ẻ': 'e2', 'ẽ': 'e3', 'é': 'e4', 'ẹ': 'e5',
        'ê': 'e6', 'ề': 'e7', 'ể': 'e8', 'ễ': 'e9', 'ế': 'e10', 'ệ': 'e11',
        # Bạn có thể thêm i, o, u tương tự, nhưng đây là những chữ cái gây lỗi nhất
    }

    def convert_word(word):
        res = ""
        for char in word.lower():
            res += dict_map.get(char, char)
        return res

    parts = full_name.strip().split()
    if not parts: return ""
    
    # Trình tự: Ưu tiên Tên cuối cùng -> sau đó là Họ lót
    last_name = convert_word(parts[-1])
    full_normalized = convert_word(" ".join(parts))
    
    return (last_name, full_normalized)

def sap_xep_danh_ba(contacts):
    if not contacts:
        print("\nDanh bạ trống.")
        return

    # Sắp xếp danh sách gốc dựa trên key Tiếng Việt
    contacts.sort(key=lambda x: vietnamese_sort_key(x['name']))
    
    print("\n✅ Đã sắp xếp danh bạ theo Tên (A-Z).")
    hien_thi_danh_ba(contacts)

def thong_ke(contacts):
    print(f"\n--- THỐNG KÊ ---")
    print(f"Tổng số liên hệ hiện có: {len(contacts)}")

def xuat_json(contacts):
    try:
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4, ensure_ascii=False)
        # Chỉ in thông báo khi người dùng chủ động chọn Xuất (Option 8)
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
    print("6. Xóa liên hệ")
    print("7. Sửa đổi liên hệ")
    print("8. Xuất file JSON (Nâng cao)")
    print("0. Thoát")
    print("===================================")

def main():
    contacts = tai_du_lieu()
    while True:
        hien_thi_menu()
        choice = input("Lựa chọn của bạn (0-8): ")
        if choice == '1': them_lien_he(contacts)
        elif choice == '2': hien_thi_danh_ba(contacts)
        elif choice == '3': tim_kiem(contacts)
        elif choice == '4': sap_xep_danh_ba(contacts)
        elif choice == '5': thong_ke(contacts)
        elif choice == '6': xoa_lien_he(contacts)
        elif choice == '7': sua_lien_he(contacts)
        elif choice == '8': 
            xuat_json(contacts)
            print(f"Đã xuất dữ liệu thành công ra {JSON_FILE}")
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()