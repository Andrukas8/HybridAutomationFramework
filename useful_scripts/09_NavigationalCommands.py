from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/register")
driver.get("https://opensource-demo.orangehrmlive.com/")

#Navigational commands
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()

