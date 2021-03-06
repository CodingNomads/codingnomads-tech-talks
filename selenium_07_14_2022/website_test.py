import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

waiting_time=1
demo_time=300

url="https://www.saucedemo.com/"
options= webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
time.sleep(waiting_time)

# time.sleep(demo_time)

## Insert User name
selected_user="standard_user"   
user_name = driver.find_element_by_id("user-name")
user_name.clear() #delete anything previously typed
user_name.send_keys(selected_user)
time.sleep(waiting_time)

## Insert password
secret_password='secret_sauce'  
password = driver.find_element_by_id("password")
password.clear() #delete anything previously typed
password.send_keys(secret_password)
time.sleep(waiting_time)

## Click the login button
login=driver.find_element_by_id("login-button")
login.click()

time.sleep(waiting_time-0.5)


## Click in something
# all_buttons=driver.find_elements_by_class_name("inventory_item_price")
all_buttons=driver.find_elements_by_tag_name("button")
cart_buttons=[]
for button in all_buttons:
    if button.text=='ADD TO CART':
        cart_buttons.append(button)

## Case 1- Buy one object
def buy_products(cart_buttons,n):
    purchased_items=random.sample(cart_buttons,n)
    for each in purchased_items:
        each.click()
        time.sleep(waiting_time)
    return()

how_many=int(input(f"\nHow many products you want to buy?\n"))
buy_products(cart_buttons,how_many) #This is a random way to select products

link=driver.find_element_by_class_name("shopping_cart_link")
link.click()
time.sleep(waiting_time)

## To proceed with paynment
proceed=driver.find_element_by_id("checkout")
proceed.click()
time.sleep(waiting_time)

first_name=driver.find_element_by_id("first-name")
first_name.clear()
first_name.send_keys("luis")
time.sleep(waiting_time)

last_name=driver.find_element_by_id("last-name")
last_name.clear()
last_name.send_keys("Hernandez")
time.sleep(waiting_time)

zip_code=driver.find_element_by_id("postal-code")
zip_code.clear()
zip_code.send_keys("10701")
time.sleep(waiting_time)

continue_button=driver.find_element_by_id("continue")
continue_button.click()
time.sleep(waiting_time)

finish=driver.find_element_by_id("finish")
finish.click()
time.sleep(waiting_time)
driver.close()