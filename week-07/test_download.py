import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = "https://the-internet.herokuapp.com"

@pytest.fixture
def driver():
    """Khởi tạo và đóng trình duyệt Chrome cho mỗi test case."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_implicit_wait(driver):
    """5.2 Implicit Waits: Thiết lập thời gian chờ ngầm định toàn cục."""
    driver.implicitly_wait(10)
    driver.get(f"{BASE_URL}/dynamic_loading/2")
    
    # Click Start
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    # Implicit wait tự động chờ tối đa 10s cho đến khi element xuất hiện trong DOM
    finish_text = driver.find_element(By.ID, "finish")
    assert "Hello World!" in finish_text.text

def test_explicit_wait_hidden_element(driver):
    """5.1 Explicit Waits & EC.visibility_of_element_located: Xử lý phần tử bị ẩn (display: none)."""
    driver.get(f"{BASE_URL}/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    wait = WebDriverWait(driver, 10)
    
    # Đợi loading bar biến mất (invisibility_of_element_located)
    wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
    
    # Đợi text "Hello World!" hiển thị (visibility_of_element_located)
    finish_element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    assert finish_element.text == "Hello World!"

def test_explicit_wait_rendered_element(driver):
    """EC.presence_of_element_located: Xử lý phần tử được render sau bằng JavaScript."""
    driver.get(f"{BASE_URL}/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    wait = WebDriverWait(driver, 10)
    
    # Đợi element có mặt trong DOM (chưa chắc đã hiển thị)
    finish_element = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    
    # Có thể kết hợp thêm đợi hiển thị
    wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    
    assert finish_element.text == "Hello World!"

def test_timeout_exception(driver):
    """7.1 Exceptions: Bắt lỗi TimeoutException khi quá thời gian chờ bằng pytest.raises."""
    driver.get(f"{BASE_URL}/dynamic_loading/1")
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    # Cố tình set thời gian chờ rất ngắn (1s) để gây ra lỗi Timeout
    wait = WebDriverWait(driver, 1)
    
    with pytest.raises(TimeoutException):
        wait.until(EC.visibility_of_element_located((By.ID, "finish")))