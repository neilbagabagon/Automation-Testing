from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as expected_conditions
import time

class DuckDuckGoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://duckduckgo.com/"

    def open(self):
        self.driver.get(self.url)
        assert "DuckDuckGo" in self.driver.title

    def search(self, query):
        search_box = self.driver.find_element(By.ID, "searchbox_input")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        assert query in self.driver.page_source

    def click_about_button(self):
        about_button = self.driver.find_element(By.LINK_TEXT, "About DuckDuckGo")
        about_button.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_is("About DuckDuckGo")
        )
        print("Current title:", self.driver.title)  # Debug
        assert self.driver.title == "About DuckDuckGo"

    def click_privacy_button(self):
        privacy_button = self.driver.find_element(By.LINK_TEXT, "Privacy Policy")
        privacy_button.click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.title_contains("DuckDuckGo Privacy Policy")
        )
        assert "DuckDuckGo Privacy Policy" in self.driver.title

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        scroll_position = self.driver.execute_script("return window.pageYOffset;")
        assert scroll_position > 0

    def browser_navigation(self):
        self.driver.back()
        assert "DuckDuckGo" in self.driver.title

        self.driver.forward()
        assert "DuckDuckGo" in self.driver.title

        self.driver.refresh()
        assert "DuckDuckGo" in self.driver.title

    def window_controls(self):
        # Maximize and check
        self.driver.maximize_window()
        assert self.driver.get_window_size()["width"] > 1000

        # Resize instead of minimize for measurable effect
        self.driver.set_window_size(600, 400)
        size = self.driver.get_window_size()
        print("Window size after resize:", size)  # Debug

        # Allow tolerance for OS/driver adjustments
        assert abs(size["width"] - 600) <= 10
        assert abs(size["height"] - 400) <= 10

        # Close at the end
        self.driver.close()

