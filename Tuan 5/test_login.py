import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # Chờ ngầm định tối đa 10 giây
    yield driver
    driver.quit() # Đóng trình duyệt sau khi test xong

# -------------------------------------------------------------------
# Test Case 1: Đăng nhập thành công với tài khoản hợp lệ
# -------------------------------------------------------------------
def test_login_success(driver):
    # 1. Truy cập trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Nhập thông tin tài khoản hợp lệ
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 3. Bấm nút Đăng nhập
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 4. Chờ tối đa 10 giây cho tới khi URL chuyển sang chứa '/secure'
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    
    # 5. Kiểm tra kết quả
    assert "/secure" in driver.current_url
    flash_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in flash_message

# -------------------------------------------------------------------
# Test Case 2: Đăng nhập thất bại do sai mật khẩu
# -------------------------------------------------------------------
def test_login_invalid_password(driver):
    # 1. Truy cập trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Nhập tên đăng nhập đúng nhưng mật khẩu sai
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")
    
    # 3. Bấm nút Đăng nhập
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 4. Kiểm tra kết quả
    assert "/login" in driver.current_url
    flash_message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in flash_message

# -------------------------------------------------------------------
# Test Case 3: Đăng nhập thất bại do sai tên đăng nhập
# -------------------------------------------------------------------
def test_login_invalid_username(driver):
    # 1. Truy cập trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Nhập tên đăng nhập không tồn tại
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 3. Bấm nút Đăng nhập
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 4. Kiểm tra kết quả
    assert "/login" in driver.current_url
    flash_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in flash_message