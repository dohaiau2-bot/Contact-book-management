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
