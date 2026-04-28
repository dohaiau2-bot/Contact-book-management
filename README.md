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

##  Bảng Tự Đánh Giá (Self-Grading Rubric)

Dựa trên yêu cầu của học phần **Programming Methods**, dưới đây là bảng tự đánh giá các tính năng đã triển khai trong dự án:

| Thành phần (Component) | Tiêu chí chi tiết (Detailed Criteria) | Trạng thái | Điểm (Points) |
| :--- | :--- | :---: | :---: |
| **1. CLI Menu System** | [cite_start]Sử dụng vòng lặp vô hạn `while True`, xử lý tốt các lựa chọn không hợp lệ mà không làm dừng chương trình. | ✅ | 1.0 |
| **2. Data Input & Validation** | Thêm bản ghi mới thành công. [cite_start]Xác thực dữ liệu số điện thoại bằng Regex và chặn tên trống. | ✅ | 1.0 |
| **3. Data Display** | [cite_start]In danh sách liên hệ dưới dạng bảng có căn lề cột rõ ràng và tiêu đề bảng. | ✅ | 1.0 |
| **4. Basic Search** | [cite_start]Tìm kiếm và xử lý chính xác liên hệ dựa trên mã ID cụ thể (trong chức năng Xóa/Sửa)[cite: 40, 74]. | ✅ | 1.0 |
| **5. Sorting Mechanism** | [cite_start]Triển khai thuật toán sắp xếp danh sách theo tên (A-Z) hỗ trợ đầy đủ ký tự Tiếng Việt. | ✅ | 1.0 |
| **6. Basic Calculation** | [cite_start]Tính toán chính xác tổng số lượng liên hệ có trong hệ thống[cite: 44, 77]. | ✅ | 1.0 |
| **7. TXT File Handling** | [cite_start]Lưu và tải dữ liệu từ tệp `contacts.txt` ổn định, không làm mất dữ liệu khi khởi động lại. | ✅ | 1.0 |
| **8. [Advanced] Complex Logic** | [cite_start]Triển khai tìm kiếm chuỗi con (substring) và thống kê phân nhóm theo tên miền Email[cite: 52, 54, 77]. | ✅ | 1.0 |
| **9. [Advanced] JSON/DBMS** | [cite_start]Xuất dữ liệu thành công ra định dạng tệp `contacts.json` cấu trúc. | ✅ | 1.0 |
| **10. Git & Modular Code** | [cite_start]Mã nguồn chia nhỏ thành các hàm chuyên biệt (Top-Down Design), có README và lịch sử Commit[cite: 58, 64, 77]. | ✅ | 1.0 |
| **TỔNG CỘNG** | | | **10.0 / 10.0** |

---
*Ghi chú: Điểm số dựa trên việc đối chiếu mã nguồn với file "Chapter 3 - Mini project.pdf".*
