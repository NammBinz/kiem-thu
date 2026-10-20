import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://the-internet.herokuapp.com/login"

import time

def measure(label, action):
    start = time.perf_counter()
    result = action()
    print(f"\n{label}: {time.perf_counter() - start:.2f}s", flush=True)
    return result

@pytest.fixture
def driver():
    start = time.perf_counter()
    browser = webdriver.Chrome()
    print(f"\nMo Chrome: {time.perf_counter() - start:.2f}s")

    yield browser

    start = time.perf_counter()
    browser.quit()
    print(f"\nDong Chrome: {time.perf_counter() - start:.2f}s")


def open_login(driver):
    start = time.perf_counter()
    driver.get(URL)
    print(f"\nTai trang: {time.perf_counter() - start:.2f}s")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "username")))


def login(driver, username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


def get_flash_message(driver):
    wait = WebDriverWait(driver, 10)
    return wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text


def test_login_success(driver):
    open_login(driver)
    login(driver, "tomsmith", "SuperSecretPassword!")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/secure")
    )

    assert "/secure" in driver.current_url
    assert "You logged into a secure area!" in get_flash_message(driver)


def test_login_invalid_password(driver):
    start = time.perf_counter()
    print("\nBAT DAU TEST", flush=True)

    # Bước 1: Mở trang
    driver.get("https://the-internet.herokuapp.com/login")
    print(f"1. Mo trang: {time.perf_counter() - start:.2f}s", flush=True)

    # Bước 2: Nhập dữ liệu
    start = time.perf_counter()
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("WrongPassword123")
    print(f"2. Nhap du lieu: {time.perf_counter() - start:.2f}s", flush=True)

    # Bước 3: Click Login
    start = time.perf_counter()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    print(f"3. Click Login: {time.perf_counter() - start:.2f}s", flush=True)

    # Bước 4: Lấy thông báo
    start = time.perf_counter()
    flash_message = driver.find_element(By.ID, "flash").text
    print(f"4. Lay thong bao: {time.perf_counter() - start:.2f}s", flush=True)

    # Bước 5: Kiểm tra
    assert "Your password is invalid!" in flash_message
    assert "/login" in driver.current_url


def test_login_invalid_username(driver):
    open_login(driver)
    login(driver, "invalid_user", "SuperSecretPassword!")

    assert "Your username is invalid!" in get_flash_message(driver)
    assert "/login" in driver.current_url
