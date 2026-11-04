# W1 – Tuần 08: Hover & Horizontal Slider

## 1. Đúng phân công

Tuần 8 – W1: **Di chuột & thanh trượt** trên `/hovers`, `/horizontal_slider`.
Nội dung API: `ActionChains`, `move_to_element`, `click_and_hold`, `move_by_offset`, `release`, `drag_and_drop_by_offset`, `perform`, `is_displayed`, `Keys.HOME`, `Keys.ARROW_RIGHT`.

## 2. Chạy trên Windows (PowerShell)

Mở Terminal **tại thư mục gốc `kiem-thu`**:

```powershell
python -m pip install -r week-08/requirements.txt
python -m pytest -v week-08/test_hover_slider.py --html=week-08/reports/report.html --self-contained-html
```

Mở `week-08/reports/report.html` bằng trình duyệt để xem báo cáo HTML. Lưu ý: Browser phải có Chrome và kết nối Internet; Selenium Manager cần tải/định vị driver tương thích.

## 3. Cấu trúc

```
week-08/
├── test_hover_slider.py    # 5 automated tests
├── requirements.txt
├── README.md
├── notes.md
├── image/                 # thêm ảnh chạy test của nhóm
└── reports/               # báo cáo HTML tạo khi chạy
```

## 4. Ghi chú kỹ thuật

- Mỗi test khởi tạo Chrome riêng qua `setUp()` và kết thúc bằng `tearDown()`.
- Slider có giá trị/step xác định từ DOM, tránh viết cứng bước tăng.
- Test chuột chỉ xác minh giá trị **tăng**, không giả định chính xác số điểm mà offset pixel làm thay đổi (phụ thuộc kích thước trình duyệt).
- Các bài test **chưa được chạy Chrome trong môi trường tạo file**; cần kiểm thử trên máy của nhóm.
- Nếu test kéo slider không ổn định trên máy khác, ghi lại cấu hình Chrome, kích thước cửa sổ và log trước khi thay đổi thao tác chuột.

## 5. Đưa lên GitHub

Trên VS Code, chuyển sang nhánh cá nhân bắt nguồn từ `week-08` (ví dụ `t08-nam`), stage `week-08/`, commit với message `T08: Nam kiem thu hover va slider`, push rồi mở PR: **base `week-08` ← compare `t08-nam`**.

**Cẩn thận:** Nếu còn file thay đổi chưa commit ở nhánh khác, kiểm tra `git status`/stash trước khi checkout. Không dùng `reset --hard` hoặc `git clean -fd`.
