from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/register")
driver.find_element(By.XPATH,"//a[normalize-space()='Facebook']").click()
driver.maximize_window()

#Conditional commands

#driver.close() # closes only one browser and doesn't close the process
driver.quit() # closes all browsers opened during teat and closes the process






