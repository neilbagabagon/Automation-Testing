from driver import driver

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.messenger.com/login/')
driver.maximize_window()
title = webdriver.title
print(title)

assert "Messenger" in title
# This is the Expected vs the Actual result


