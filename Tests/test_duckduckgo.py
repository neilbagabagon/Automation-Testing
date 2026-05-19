import pytest
from Pages.duckduckgo_page import DuckDuckGoPage
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search(driver):
    page = DuckDuckGoPage(driver)
    page.open()
    page.search("Selenium Python")

def test_buttons(driver):
    page = DuckDuckGoPage(driver)
    page.open()
    page.click_about_button()
    page.open()
    page.click_privacy_button()

def test_scroll(driver):
    page = DuckDuckGoPage(driver)
    page.open()
    page.scroll_page()

def test_browser_navigation(driver):
    page = DuckDuckGoPage(driver)
    page.open()
    page.search("QA Engineer")
    page.browser_navigation()

def test_window_controls(driver):
    page = DuckDuckGoPage(driver)
    page.open()
    page.window_controls()
