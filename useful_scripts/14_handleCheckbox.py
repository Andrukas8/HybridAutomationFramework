from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

# 1) Select specific checkbox on the list
# driver.find_element(By.XPATH,"//input[1]").click()

# 2) Capturing all checkboxes
checkBoxes = driver.find_elements(By.XPATH,"//input")
for checkBox in checkBoxes:
    checkBox.click()