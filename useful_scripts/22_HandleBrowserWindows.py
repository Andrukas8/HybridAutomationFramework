from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs = driver.window_handles

parentWindowID = windowsIDs[0]
childwindowID = windowsIDs[1]
print(parentWindowID)
print(childwindowID)

driver.switch_to.window(childwindowID)
print("Child window  = ",driver.title)

driver.switch_to.window(parentWindowID)
print("Parent window = ",driver.title)

driver.quit()

#driver.close()