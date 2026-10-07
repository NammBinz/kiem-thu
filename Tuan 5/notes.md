# GHI CHÚ TUẦN 05 (WEEK-05)

**Họ và tên:** Phạm Đình Trung  

---

## 1. Trả lời câu hỏi đọc tài liệu (trước buổi học)

### Câu 1: Với ô tên đăng nhập ở trang `/login`, nên xác định bằng cách nào là ổn định nhất, vì sao?
- **Trả lời:**
  - **Cách xác định ổn định nhất:** Sử dụng thuộc tính **`id`** (ví dụ: `By.ID, "username"`).
  - **Lý do:**
    1. `id` là thuộc tính duy nhất (unique) trên toàn bộ cây DOM của trang web, giúp Selenium định vị chính xác phần tử mà không sợ bị nhầm lẫn với các ô nhập khác.
    2. Thuộc tính `id` thường do lập trình viên cố định trong mã nguồn, ít bị thay đổi khi giao diện CSS hoặc layout được làm mới.
    3. Tìm kiếm theo `id` có tốc độ xử lý nhanh hơn nhiều so với việc duyệt cây DOM bằng các câu lệnh XPath hoặc CSS Selector phức tạp.

---

### Câu 2: Muốn nhập chữ vào một ô thì dùng lệnh gì?
- **Trả lời:**
  - **Lệnh sử dụng:** Dùng phương thức **`.send_keys("nội_dung_cần_nhập")`**.
  - **Ví dụ trong code:**
    ```python
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    ```
  - **Lưu ý:** Trước khi nhập nội dung mới vào ô đã có sẵn chữ, nên sử dụng `.clear()` để làm sạch ô nhập liệu trước khi gọi `.send_keys()`.

---

### Câu 3: Làm thế nào để biết `id` của một ô nhập trên trang?
- **Trả lời:**
  1. Mở trang web cần kiểm thử trên trình duyệt Google Chrome.
  2. Nhấn phím **`F12`** (hoặc click chuột phải $\rightarrow$ chọn **Inspect**) để mở **Chrome DevTools**.
  3. Bấm vào biểu tượng con trỏ chỉ trỏ ở góc trên bên trái bảng DevTools.
  4. Nhấp chuột trực tiếp vào ô nhập liệu trên giao diện web.
  5. Thẻ HTML tương ứng sẽ được highlight trong tab **Elements**. Quan sát và lấy giá trị nằm trong thuộc tính `id="..."` (ví dụ: `<input id="username" type="text">`).

---

### Câu 4: Nếu kết quả thực tế khác mong đợi thì `pytest` báo gì?
- **Trả lời:**
  - **Báo lỗi:** `pytest` sẽ đánh dấu test case đó là **`FAILED`** và ném ra lỗi **`AssertionError`**.
  - **Thông tin hiển thị:**
    1. Dòng code chứa câu lệnh `assert` bị sai.
    2. Sự khác biệt cụ thể giữa kết quả thực tế thu được (`Actual`) và kết quả mong đợi (`Expected`).
    3. Bảng tổng kết số lượng test case vượt qua và thất bại ở cuối phiên chạy (ví dụ: `1 failed, 2 passed`).

---

## 2. Bài học thu được & Nhật ký làm việc với AI

### Bài học thu được:
- Nắm vững quy trình 3 bước cốt lõi trong Automation Test giao diện: **Định vị phần tử (Locator)** $\rightarrow$ **Thao tác (send_keys / click)** $\rightarrow$ **Kiểm tra kết quả (assert)**.
- Hiểu và vận dụng thành công `WebDriverWait` kết hợp với `expected_conditions` (EC) để xử lý các tác vụ bất đồng bộ như chờ chuyển trang (`url_contains`) hoặc chờ Alert xuất hiện thay vì dùng `time.sleep()` cứng.
- Biết cách đọc và phân tích các thông báo lỗi phổ biến của Selenium/pytest như `ERR_CONNECTION_REFUSED`, `NoSuchElementException`, `AssertionError`, và `NameError`.

### Nhật ký sử dụng AI hỗ trợ:
- **Câu hỏi/Vấn đề đặt ra cho AI:** 
  - Hỏi cách sửa lỗi `AssertionError` khi kiểm tra URL do trình duyệt chưa kịp chuyển hướng (`redirect`) sau khi bấm Đăng nhập.
  - Hỏi cách xử lý lỗi `NameError: name 'WebDriverWait' is not defined`.
- **Đánh giá câu trả lời của AI:**
  - AI phản hồi chính xác 100%. AI đã giải thích rõ nguyên nhân là do bất đồng bộ thời gian load trang và hướng dẫn import đầy đủ thư viện `from selenium.webdriver.support.ui import WebDriverWait` cùng điều kiện `EC.url_contains("/secure")`.
- **Kết quả:** Đã áp dụng thành công gợi ý của AI vào code, giúp toàn bộ 3 bài test case chạy qua thành công (`3 passed`).