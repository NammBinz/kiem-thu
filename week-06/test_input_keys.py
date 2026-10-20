# python -m pip install selenium pytest
# python -m pytest -v week-06/test_input_keys.py

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://the-internet.herokuapp.com"
TIMEOUT = 10


class TestInputAndSpecialKeys(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def tearDown(self):
        self.driver.quit()

    # Mở trang kiểm tra phím đặc biệt
    def open_key_presses(self):
        self.driver.get(f"{BASE_URL}/key_presses")
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, "target"))
        )

    # Kiểm tra kết quả hiển thị khi nhấn phím
    def assert_key_result(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element((By.ID, "result"), expected)
        )

        actual = self.driver.find_element(By.ID, "result").text
        self.assertEqual(actual, expected)

    # Mở trang nhập số
    def open_number_input(self):
        self.driver.get(f"{BASE_URL}/inputs")
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
        )

    def test_enter_key_is_detected(self):
        self.open_key_presses()

        body = self.driver.find_element(By.TAG_NAME, "body")
        body.click()
        body.send_keys(Keys.ENTER)

        self.assert_key_result("You entered: ENTER")

    def test_tab_key_is_detected(self):
        field = self.open_key_presses()
        field.send_keys(Keys.TAB)

        self.assert_key_result("You entered: TAB")

    def test_arrow_up_key_is_detected(self):
        field = self.open_key_presses()
        field.send_keys(Keys.ARROW_UP)

        self.assert_key_result("You entered: UP")

    def test_number_input_and_clear(self):
        number_field = self.open_number_input()

        number_field.clear()
        number_field.send_keys("123")
        self.assertEqual(number_field.get_attribute("value"), "123")

        number_field.clear()
        self.assertEqual(number_field.get_attribute("value"), "")

    def test_arrow_up_increments_number(self):
        number_field = self.open_number_input()

        number_field.clear()
        number_field.send_keys("100")
        number_field.send_keys(Keys.ARROW_UP)

        self.assertEqual(number_field.get_attribute("value"), "101")


if __name__ == "__main__":
    unittest.main()
