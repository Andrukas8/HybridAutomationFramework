from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
#driver.get("http://orangehrm.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

myWait = WebDriverWait(driver,10) # explicit wait declaration

driver.get("https://www.google.com")
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
searchBox = (driver.find_element(By.NAME,"q"))
searchBox.send_keys("Selenium")
searchBox.submit()

searchLink = myWait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchLink.click()



