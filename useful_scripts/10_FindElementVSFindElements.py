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

# Single element
#element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#element.send_keys("Apple Mcbook Pro")

# Multiple elements
elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
for count, element in enumerate(elements):
    print(count,element.text)
time.sleep(2)
driver.quit()

