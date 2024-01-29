from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#Conditional commands
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status: ",searchbox.is_displayed())
print("Enabled status: ",searchbox.is_enabled())
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
rd_male.click()
rd_female.click()
print("Radio Select Status Male   : ",rd_male.is_selected())
print("Radio Select Status Female : ",rd_female.is_selected())

driver.close()





