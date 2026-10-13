python -m pip show selenium# Bài thực hành kiểm thử tự động - Tuần 4

## Yêu cầu
- Python
- Google Chrome
- Selenium
- pytest

## Cài thư viện

```bash
python -m pip install selenium pytest
```

## Chạy bài kiểm thử

Đứng tại thư mục gốc của project và chạy:

```bash
python -m pytest tuan-04/test_smoke.py -v
```

Nếu bài kiểm thử chạy đúng, pytest sẽ báo `PASSED`.

## Nội dung bài
Bài `test_smoke.py` mở trang https://the-internet.herokuapp.com/ bằng Chrome và kiểm tra tiêu đề trang có bằng `The Internet` hay không.

## Ảnh kết quả
Ảnh chụp màn hình kết quả chạy thành công của từng thành viên được đặt trong thư mục:

`tuan-04/anh/`
