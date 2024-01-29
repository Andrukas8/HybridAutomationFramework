from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# opens alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

alertWindow = driver.switch_to.alert
print(alertWindow.text)

alertWindow.send_keys("Hello")
time.sleep(2)
alertWindow.accept() # OK button
alertWindow.dismiss() # Cancel button


