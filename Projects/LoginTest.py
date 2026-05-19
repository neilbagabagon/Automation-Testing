from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.maximize_window()

url_link = "https://www.saucedemo.com/"
browser.get(url_link)

time.sleep(5)

username = "standard_user"
password = "secret_sauce"

user_field = browser.find_element(By.ID, "user-name")
pass_field = browser.find_element(By.ID, "password")

user_field.send_keys(username)
pass_field.send_keys(password)

login_button = browser.find_element(By.ID, "login-button")
login_button.click()

add_to_cart_btns = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light",
               "add-to-cart-test.allthethings()-t-shirt-(red)", "add-to-cart-sauce-labs-onesie",
                "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-fleece-jacket"]
for each_cart_btn in add_to_cart_btns:
     add_button = browser.find_element(By.ID, each_cart_btn)
     add_button.click()

cart = browser.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
cart.click()

remove_buttons = ["remove-sauce-labs-bike-light", "remove-test.allthethings()-t-shirt-(red)",
                 "remove-sauce-labs-onesie", "remove-sauce-labs-backpack",
                 "remove-sauce-labs-bolt-t-shirt", "remove-sauce-labs-fleece-jacket"]

for each_remove_btn in remove_buttons:
     remove_btn = browser.find_element(By.ID, each_remove_btn)
     remove_btn.click()

continue_shop = browser.find_element(By.ID, "continue-shopping")
continue_shop.click()

cart.click()

checkout_btn = browser.find_element(By.ID, "checkout")
checkout_btn.click()

first_name = "Neil Jordan"
last_name = "Bagabagon"
zip_code = "4009"

FirstName_field = browser.find_element(By.ID, "first-name")
LastName_field = browser.find_element(By.ID, "last-name")
Zip_field = browser.find_element(By.ID, "postal-code")

FirstName_field.send_keys(first_name)
LastName_field.send_keys(last_name)
Zip_field.send_keys(zip_code)

continue_checkout_btn = browser.find_element(By.ID, "continue")
continue_checkout_btn.click()

# item_quantity = browser.find_element(By.CLASS_NAME, "cart_quantity")
# assert len(item_quantity) == 4, f"Expected 4 quantities, got {len(item_quantity)}"

time.sleep(5)
browser.quit()

"""
This
is
a
Multi-line
comment
"""
