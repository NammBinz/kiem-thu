## Mục tiêu

Dùng Selenium Python điều khiển di chuột, kéo/thả thanh trượt và phím đặc biệt. Xác minh bằng assertion, xuất báo cáo HTML bằng pytest-html.

## Test cases

| ID | Test | Bước chính | Kết quả mong đợi |
|---|---|---|---|
| T08-01 | Hover từng user | `move_to_element` qua 3 ảnh | Hiện caption, đúng `name: user1/2/3`, đúng link |
| T08-02 | Caption ẩn ban đầu | Mở `/hovers`, chưa hover | Chú thích cả 3 user đều ẩn |
| T08-03 | Slider bằng phím | HOME, RIGHT x2 | Giá trị tăng 2 bước (`step`), số hiển thị khớp |
| T08-04 | Slider bằng chuột | click_and_hold → move_by_offset → release | Giá trị tăng, số hiển thị khớp |
| T08-05 | Drag & drop offset | drag_and_drop_by_offset | Giá trị tăng, số hiển thị khớp |

## Kết quả thực tế (điền sau khi chạy)

- **Ngày chạy:** [Điền]
- **Thiết bị / trình duyệt:** [Điền]
- **Tổng:** [Điền] passed, [Điền] failed
- **Ảnh Terminal:** `image/Nam.png` (hoặc ảnh của người thực hiện)
- **Báo cáo HTML:** `reports/report.html` (nếu giảng viên yêu cầu lưu kèm)
- **Lỗi thực tế và cách xử lý:** [Ghi theo log, nếu có]
