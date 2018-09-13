import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import time

# Initiates chrome driver which allows your google chrome to be controlled by automated test software
driver = webdriver.Chrome(executable_path='/Users/nadimyounes/Downloads/chromedriver')


#Function to log in twitter
def log_in(driver,username,password):
 #open the web page in the browser:
    driver.get("https://twitter.com/login")

    # find the boxes for username and password(through inspect element)
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    # enter your username:
    username_field.send_keys(username)
    driver.implicitly_wait(10)

    # enter your password:
    password_field.send_keys(password)
    driver.implicitly_wait(10)

    # click the "Log In" button:
    driver.find_element_by_class_name("EdgeButtom--medium").click()

    return

log_in(driver,'***email***','**password***')

search = driver.find_element_by_name('q')
search.send_keys("elonmusk")
search.send_keys(Keys.RETURN)

time.sleep(10) # sleep for 10 seconds so you can see the results
