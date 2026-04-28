# Contact-book-management
mini project for DHS course

# Giới thiệu
Đây là dự án nhỏ (Mini-Project) thuộc học phần Phương pháp lập trình (Programming Methods). Ứng dụng được xây dựng theo mô hình Lập trình thủ tục (Procedural Programming) bằng ngôn ngữ Python, nhằm quản lý danh sách liên hệ cá nhân một cách có hệ thống.

Chương trình cho phép người dùng lưu trữ thông tin (ID, Tên, Số điện thoại, Email) bền vững thông qua tệp tin văn bản và cung cấp các tính năng tìm kiếm, thống kê nâng cao.

# Tính năng nổi bật
 ## 1. Quản lý cơ bản (CRUD)
Thêm liên hệ: Tự động cấp ID trống nhỏ nhất, kiểm tra định dạng Số điện thoại và Email.

Hiển thị: Danh sách liên hệ được trình bày dưới dạng bảng đẹp mắt, rõ ràng.

Sửa đổi: Cho phép cập nhật thông tin liên hệ dựa trên mã ID.

Xóa: Loại bỏ liên hệ khỏi hệ thống (cập nhật đồng bộ cả file .txt và .json).

 ## 2. Xử lý nâng cao (Advanced Logic)
Tìm kiếm chuỗi con (Substring Search): Tìm kiếm liên hệ dựa trên một phần tên người dùng nhập vào.

Lọc theo điều kiện (Filtering): Lọc danh sách liên hệ theo đầu số nhà mạng (035, 090...) hoặc theo tên miền Email (gmail.com, yahoo.com...).

Thống kê theo nhóm (Grouped Statistics): Tự động phân loại và đếm số lượng liên hệ theo từng nhà cung cấp Email.

 ## 3. Sắp xếp & Dữ liệu
Sắp xếp Tiếng Việt (Vietnamese Sorting): Thuật toán sắp xếp danh sách theo tên (A-Z) hỗ trợ đầy đủ các ký tự có dấu đặc thù của Tiếng Việt.

Lưu trữ bền vững: Dữ liệu tự động lưu vào tệp contacts.txt.

Xuất file JSON: Hỗ trợ xuất dữ liệu sang định dạng .json để sử dụng cho các ứng dụng khác.

#  Cài đặt
Yêu cầu hệ thống:

Máy tính đã cài đặt Python 3.x.

Tải mã nguồn:

Tải tệp tin main.py (hoặc tên tệp bạn đặt) về máy.

Chuẩn bị tệp dữ liệu:

Chương trình sẽ tự động tạo tệp contacts.txt trong lần chạy đầu tiên nếu chưa có.

#  Cách sử dụng
Mở Terminal hoặc Command Prompt tại thư mục chứa mã nguồn.

Chạy chương trình bằng lệnh:

Bash
python main.py
Sử dụng các phím số từ 0 đến 7 trên bàn phím để chọn chức năng tương ứng từ Menu:

1: Nhập thông tin để thêm liên hệ mới.

2: Xem toàn bộ danh sách liên hệ hiện có.

3: Vào Menu phụ để tìm kiếm theo tên hoặc lọc theo SĐT/Email.

4: Sắp xếp lại danh bạ theo thứ tự bảng chữ cái Tiếng Việt.

5: Xem báo cáo thống kê tổng số và chi tiết theo nhóm Email.

6: Nhập mã ID để xóa liên hệ.

7: Xuất dữ liệu hiện tại ra tệp contacts.json.

0: Lưu dữ liệu và thoát chương trình.

# Cấu trúc thư mục
main.py: Tệp mã nguồn chính chứa toàn bộ logic chương trình.

contacts.txt: Tệp lưu trữ dữ liệu thô (ngăn cách bởi dấu |).

contacts.json: Tệp xuất dữ liệu định dạng JSON (dùng cho tính năng nâng cao).

README.md: Tệp hướng dẫn này.

| Thành phần (Component) | Tiêu chí chi tiết | Giải thích (Cách thực hiện trong mã nguồn) | Trạng thái | Điểm |
| :--- | :--- | :--- | :---: | :---: |
| **1. CLI Menu System** | Menu tương tác dùng vòng lặp vô hạn, xử lý lỗi nhập. | [cite_start]Sử dụng vòng lặp `while True` trong hàm `main()` và khối `else` để báo lỗi khi người dùng nhập sai lựa chọn. | ✅ | 1.0 |
| **2. Data Input & Validation** | Thêm bản ghi mới và xác thực kiểu dữ liệu. | [cite_start]Hàm `kiem_tra_sdt` dùng Regex để chặn định dạng sai; hàm `them_lien_he` kiểm tra tên trống và SĐT trùng lặp. | ✅ | 1.0 |
| **3. Data Display** | In bản ghi rõ ràng, căn lề chuẩn theo bảng. | [cite_start]Hàm `hien_thi_danh_ba` sử dụng `f-string` với định dạng căn lề trái (ví dụ: `:<25`) để các cột luôn thẳng hàng. | ✅ | 1.0 |
| **4. Basic Search** | Tìm kiếm theo ID hoặc Tên chính xác. | [cite_start]Hàm `xoa_lien_he` và logic trong quản lý sử dụng so sánh trực tiếp để tìm chính xác liên hệ theo mã định danh. | ✅ | 1.0 |
| **5. Sorting Mechanism** | Sắp xếp theo ít nhất một trường dữ liệu. | [cite_start]Hàm `sap_xep_danh_ba` kết hợp với `vietnamese_sort_key` để sắp xếp tên theo chuẩn bảng chữ cái Tiếng Việt (A-Z). | ✅ | 1.0 |
| **6. Basic Calculation** | Tính toán thống kê cơ bản (tổng, đếm). | [cite_start]Hàm `thong_ke` sử dụng hàm `len(contacts)` để tính tổng số lượng bản ghi hiện có trong hệ thống. | ✅ | 1.0 |
| **7. TXT File Handling** | Lưu và tải dữ liệu từ tệp .txt bền vững. | [cite_start]Triển khai qua hai hàm `tai_du_lieu` (đọc tệp khi khởi động) và `luu_du_lieu` (ghi lại thay đổi sau mỗi thao tác). | ✅ | 1.0 |
| **8. [Advanced] Complex Logic** | Tìm kiếm chuỗi con hoặc thống kê theo nhóm. | [cite_start]Hàm `tim_kiem_va_loc` hỗ trợ tìm kiếm khớp một phần (substring) và `thong_ke` phân loại liên hệ theo tên miền email. | ✅ | 1.0 |
| **9. [Advanced] JSON/DBMS** | Xuất/Nhập dữ liệu dùng tệp cấu trúc .json. | [cite_start]Hàm `xuat_json` sử dụng thư viện `json` của Python để chuyển đổi danh sách dictionary thành tệp JSON có định dạng. | ✅ | 1.0 |
| **10. Git & Modular Code** | Dùng GitHub, có README, code chia theo hàm. | [cite_start]Code được thiết kế theo kiểu Top-Down, mỗi hàm đảm nhận một nhiệm vụ duy nhất (Single Responsibility). | ✅ | 1.0 |
| **TỔNG CỘNG** | | | | **10.0** |
