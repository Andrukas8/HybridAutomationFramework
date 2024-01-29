from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
searchbox.clear()
searchbox.send_keys("Searching item")
print("result of text: ",searchbox.text)
print("result of get_attribute: ",searchbox.get_attribute('value'))
driver.quit()

