from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()




