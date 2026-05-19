import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the browser.
    Ensures clean setup and teardown for each test.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_homepage_loads(driver):
    """
    Verify that the DuckDuckGo homepage loads successfully
    and the search bar is visible.
    """
    driver.get("https://duckduckgo.com/")
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "searchbox_input"))
    )
    assert search_box.is_displayed(), "Search bar should be visible on homepage"


def test_search_results(driver):
    """
    Perform a search for 'QA Automation' and assert that results are displayed.
    """
    driver.get("https://duckduckgo.com/")
    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.send_keys("QA Automation")
    search_box.send_keys(Keys.RETURN)

    # Wait until results container is visible
    results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article"))
    )
    assert len(results) > 0, "Search results should be displayed"


def test_about_page_navigation(driver):
    """
    Validate that the 'About' link in the footer navigates to the correct page.
    """
    driver.get("https://duckduckgo.com/")
    about_link = driver.find_element(By.LINK_TEXT, "About DuckDuckGo")
    about_link.click()

    WebDriverWait(driver, 10).until(
        EC.title_is("About DuckDuckGo")
    )
    assert driver.title == "About DuckDuckGo", "Should navigate to About page"


def test_search_suggestions(driver):
    """
    Ensure the search suggestions dropdown appears when typing a query.
    """
    driver.get("https://duckduckgo.com/")
    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.send_keys("QA")

    suggestions = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".searchbox_suggestions"))
    )
    assert len(suggestions) > 0, "Search suggestions should appear when typing"


def test_images_tab(driver):
    """
    Confirm that the 'Images' tab displays image results for a given query.
    """
    driver.get("https://duckduckgo.com/")
    search_box = driver.find_element(By.ID, "searchbox_input")
    search_box.send_keys("QA Automation")
    search_box.send_keys(Keys.RETURN)

    # Click on the Images tab
    images_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Images"))
    )
    images_tab.click()

    # Wait for image results to load
    image_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".tile--img"))
    )
    assert len(image_results) > 0, "Image results should be displayed"
