from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.switch_to.frame("frame-one796456169")

driver.find_element(By.PARTIAL_LINK_TEXT,"Powered by").click()
driver.switch_to.default_content() # switching to the main page
#driver.find_element(By.LINK_TEXT,"")




