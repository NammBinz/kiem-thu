# Ghi chú tuần 4

## Những gì em đã học được

Tuần này em cài Python, Selenium, pytest và Chrome để bắt đầu làm kiểm thử tự động trên web.

Em hiểu một bài Selenium cơ bản sẽ có các bước:
1. Khởi tạo WebDriver để mở trình duyệt.
2. Dùng `driver.get()` để vào trang cần kiểm thử.
3. Thực hiện hoặc lấy thông tin cần kiểm tra.
4. Dùng `assert` để so sánh kết quả thực tế với kết quả mong đợi.
5. Dùng `driver.quit()` để đóng trình duyệt.

Em cũng chạy thử `test_smoke.py`. Bài này dùng để kiểm tra nhanh hệ thống và xác nhận môi trường Selenium đã hoạt động. Trong bài tuần 4, test mở trang the-internet và kiểm tra tiêu đề trang là `The Internet`.

Khi cố ý sửa expected result thành một giá trị sai, pytest báo FAILED. Qua đó em hiểu test PASS khi kết quả thực tế đúng với expected result và FAIL khi hai giá trị không khớp.

## Trả lời phần đọc tài liệu

**Một script Selenium gồm những bước nào?**

Một script cơ bản gồm: mở WebDriver, truy cập trang web, tìm/lấy thông tin hoặc thao tác trên trang, kiểm tra kết quả bằng assertion và đóng WebDriver.

**Mỗi bước ứng với dòng nào trong bài test_smoke?**

- `driver = webdriver.Chrome()` : mở trình duyệt và tạo WebDriver.
- `driver.get(...)` : truy cập trang cần kiểm thử.
- `driver.title` : lấy tiêu đề hiện tại của trang.
- `assert driver.title == "The Internet"` : kiểm tra actual result với expected result.
- `driver.quit()` : đóng trình duyệt sau khi chạy xong.

## Lỗi gặp khi cài/chạy

Phần này em sẽ bổ sung đúng lỗi mình gặp trên máy nếu có.

Ví dụ:
- Nếu báo không tìm thấy thư viện Selenium: chạy `python -m pip install selenium`.
- Nếu pytest không chạy được: chạy bằng `python -m pytest` thay vì chỉ gõ `pytest`.

## Sử dụng AI

Em có dùng AI để hỏi:
- `test_smoke` là gì.
- Cấu trúc cơ bản của một Selenium script.
- Cách hiểu từng dòng code trong bài kiểm thử tuần 4.

Sau đó em đối chiếu lại với tài liệu Selenium. Em hiểu thêm rằng smoke test là bài kiểm tra nhanh các chức năng cơ bản, còn `assert` là phần quyết định bài kiểm thử PASS hay FAIL dựa trên kết quả mong đợi.
