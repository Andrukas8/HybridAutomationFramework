from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


#Application commands
print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()




