"""W1 – Tuần 08: Hover và Horizontal Slider trên The Internet.

Chạy từ thư mục gốc repository:
    python -m pytest -v week-08/test_hover_slider.py \
        --html=week-08/reports/report.html --self-contained-html
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://the-internet.herokuapp.com"
TIMEOUT = 10


class TestHoverAndSlider(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(20)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def tearDown(self):
        self.driver.quit()

    def open_hovers(self):
        self.driver.get(f"{BASE_URL}/hovers")
        figures = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".figure"))
        )
        self.assertEqual(len(figures), 3, "Trang phải có đúng 3 ảnh người dùng")
        return figures

    def open_slider(self):
        self.driver.get(f"{BASE_URL}/horizontal_slider")
        return self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']"))
        )

    def slider_value(self):
        slider = self.driver.find_element(By.CSS_SELECTOR, "input[type='range']")
        displayed = self.driver.find_element(By.ID, "range").text
        return float(slider.get_attribute("value")), float(displayed)

    def test_hover_shows_user_details(self):
        """Di chuột qua từng ảnh: chú thích đúng người và link hiển thị."""
        figures = self.open_hovers()
        for index, figure in enumerate(figures, start=1):
            with self.subTest(user=index):
                ActionChains(self.driver).move_to_element(figure).perform()
                caption = figure.find_element(By.CSS_SELECTOR, ".figcaption")
                self.wait.until(lambda driver: caption.is_displayed())
                self.assertTrue(caption.is_displayed())
                self.assertEqual(
                    caption.find_element(By.TAG_NAME, "h5").text,
                    f"name: user{index}",
                )
                link = caption.find_element(By.TAG_NAME, "a")
                self.assertTrue(link.is_displayed())
                self.assertTrue(link.get_attribute("href").endswith(f"/users/{index}"))

    def test_hover_details_hidden_before_hover(self):
        """Chưa hover thì chú thích người dùng không hiển thị."""
        figures = self.open_hovers()
        for index, figure in enumerate(figures, start=1):
            with self.subTest(user=index):
                caption = figure.find_element(By.CSS_SELECTOR, ".figcaption")
                self.assertFalse(caption.is_displayed())

    def test_slider_keyboard_home_and_right(self):
        """HOME về min, 2 lần RIGHT tăng 2 bước theo thuộc tính step."""
        slider = self.open_slider()
        slider.send_keys(Keys.HOME)
        minimum = float(slider.get_attribute("min") or 0)
        step = float(slider.get_attribute("step") or 1)
        self.wait.until(lambda driver: self.slider_value()[0] == minimum)

        slider.send_keys(Keys.ARROW_RIGHT, Keys.ARROW_RIGHT)
        expected = minimum + 2 * step
        self.wait.until(lambda driver: self.slider_value()[0] == expected)
        actual_input, actual_display = self.slider_value()
        self.assertEqual(actual_input, expected)
        self.assertEqual(actual_display, expected)

    def test_slider_mouse_click_hold_move_release(self):
        """Giữ chuột, kéo ngang rồi thả: giá trị slider phải tăng."""
        slider = self.open_slider()
        slider.send_keys(Keys.HOME)
        initial, _ = self.slider_value()
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(35, 0).release().perform()
        self.wait.until(lambda driver: self.slider_value()[0] > initial)
        actual_input, actual_display = self.slider_value()
        self.assertGreater(actual_input, initial)
        self.assertEqual(actual_input, actual_display)

    def test_slider_drag_and_drop_by_offset(self):
        """Kéo thanh trượt theo độ lệch bằng drag_and_drop_by_offset."""
        slider = self.open_slider()
        slider.send_keys(Keys.HOME)
        initial, _ = self.slider_value()
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 40, 0).perform()
        self.wait.until(lambda driver: self.slider_value()[0] > initial)
        actual_input, actual_display = self.slider_value()
        self.assertGreater(actual_input, initial)
        self.assertEqual(actual_input, actual_display)


if __name__ == "__main__":
    unittest.main()
