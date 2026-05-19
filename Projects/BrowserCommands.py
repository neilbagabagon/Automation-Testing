import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

url_link = "https://opensource-demo.orangehrmlive.com/"
browser.get(url_link)
time.sleep(3)
browser.maximize_window()

forgot_link = browser.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")
forgot_link.click()
time.sleep(3)

browser.back()
time.sleep(3)

browser.forward()
time.sleep(3)

browser.refresh()
time.sleep(3)

browser.quit()