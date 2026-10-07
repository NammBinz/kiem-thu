# KỊCH BẢN KIỂM THỬ CHỨC NĂNG ĐĂNG NHẬP (WEEK-05)

**Trang web kiểm thử:** https://the-internet.herokuapp.com/login
**Đối tượng:** Chức năng Đăng nhập (Login)

---

## Test Case 1: Đăng nhập thành công với tài khoản hợp lệ

* **Mục tiêu:** Kiểm tra hệ thống cho phép người dùng đăng nhập thành công khi nhập đúng Tên đăng nhập và Mật khẩu.
* **Dữ liệu đầu vào:**
  * Tên đăng nhập: `tomsmith`
  * Mật khẩu: `SuperSecretPassword!`
* **Các bước thực hiện:**
  1. Truy cập đường dẫn `https://the-internet.herokuapp.com/login`.
  2. Tìm ô nhập "Username" (bằng `id="username"`) và nhập `tomsmith`.
  3. Tìm ô nhập "Password" (bằng `id="password"`) và nhập `SuperSecretPassword!`.
  4. Nhấn nút "Login" (bằng `CSS Selector`: `button[type='submit']`).
* **Kết quả mong đợi:**
  * Hệ thống chuyển hướng người dùng sang URL chứa đường dẫn `/secure`.
  * Hiển thị thông báo thành công chứa nội dung: `"You logged into a secure area!"`.

---

## Test Case 2: Đăng nhập thất bại do sai mật khẩu

* **Mục tiêu:** Kiểm tra hệ thống ngăn chặn đăng nhập và báo lỗi khi nhập đúng Tên đăng nhập nhưng sai Mật khẩu.
* **Dữ liệu đầu vào:**
  * Tên đăng nhập: `tomsmith`
  * Mật khẩu: `WrongPassword123`
* **Các bước thực hiện:**
  1. Truy cập đường dẫn `https://the-internet.herokuapp.com/login`.
  2. Tìm ô nhập "Username" và nhập `tomsmith`.
  3. Tìm ô nhập "Password" và nhập `WrongPassword123`.
  4. Nhấn nút "Login".
* **Kết quả mong đợi:**
  * Người dùng vẫn ở lại trang đăng nhập (URL chứa `/login`).
  * Hiển thị thông báo lỗi có nội dung: `"Your password is invalid!"`.

---

## Test Case 3: Đăng nhập thất bại do Tên đăng nhập không tồn tại

* **Mục tiêu:** Kiểm tra hệ thống ngăn chặn đăng nhập và báo lỗi khi nhập Tên đăng nhập không tồn tại trong hệ thống.
* **Dữ liệu đầu vào:**
  * Tên đăng nhập: `invalid_user`
  * Mật khẩu: `SuperSecretPassword!`
* **Các bước thực hiện:**
  1. Truy cập đường dẫn `https://the-internet.herokuapp.com/login`.
  2. Tìm ô nhập "Username" và nhập `invalid_user`.
  3. Tìm ô nhập "Password" và nhập `SuperSecretPassword!`.
  4. Nhấn nút "Login".
* **Kết quả mong đợi:**
  * Người dùng vẫn ở lại trang đăng nhập (URL chứa `/login`).
  * Hiển thị thông báo lỗi có nội dung: `"Your username is invalid!"`.