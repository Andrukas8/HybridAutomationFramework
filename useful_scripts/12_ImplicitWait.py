from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(10) # seconds of implicit wait

driver.get("https://www.google.com")
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
searchBox = (driver.find_element(By.NAME,"q"))
searchBox.send_keys("Selenium")
searchBox.submit()
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

