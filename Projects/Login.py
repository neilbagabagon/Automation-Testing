import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#Declare a variable of the webdriver
driver = webdriver.Edge() #Defined a variable and selected the preferred browser. (.Chrome .Edge .Firefox etc.)
driver.maximize_window() #This is to maximize the browser to your window.

#Declare a variable so you won't need to use the actual username or password.
username = "standard_user" #Defined a variable. "standard_user" is the actual username.
password = "secret_sauce" #Defined a variable. "secret_sauce" is the actual password.


#Select and open the link
login_url = "https://www.saucedemo.com/" #This is the selected link to test that is defined inside a variable.
driver.get(login_url) #This is to open the link using .get method

#Locate Fields
username_field = driver.find_element(By.ID, "user-name") #This is to find the field using .find_element method and using .ID as locator that is declared to a variable in username.
password_field = driver.find_element(By.ID, "password") #This is to find the field using .find_element method and using .ID as locator that is declared to a variable in password.

username_field.send_keys(username) #This is to send the keys/text to the field username
password_field.send_keys(password) #This is to send the keys/text to the field password


login_button = driver.find_element(By.ID, "login-button") #Declared a variable of finding the login button.
assert not login_button.get_attribute("disabled") #assert to differentiate actual to expected result making sure that the button is not disabled.
login_button.click() #To click the button

success_element = driver.find_element(By.CSS_SELECTOR, ".title") #Declared a variable of finding something after logging in to make sure the login is successful.
assert success_element.text == "Products" #Assertion to differentiate actual and expected value.

cart_button0 = driver.find_elements(By.ID, "add-to-cart-sauce-labs-backpack")
cart_button0[0].click()

cart_button0 = driver.find_elements(By.ID, "add-to-cart-sauce-labs-bike-light")
cart_button0[0].click()

cart_button0 = driver.find_elements(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
cart_button0[0].click()


time.sleep(10) #Waiting time before the browser closes.