from selenium import webdriver


def test_smoke():
    # Mở trình duyệt Chrome
    driver = webdriver.Chrome()

    try:
        # Truy cập trang web dùng để thực hành
        driver.get("https://the-internet.herokuapp.com/")

        # Kiểm tra tiêu đề trang có đúng như yêu cầu không
        assert driver.title == "The Internet"

    finally:
        # Đóng trình duyệt sau khi kiểm thử xong
        driver.quit()