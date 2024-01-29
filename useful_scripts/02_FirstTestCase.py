# Test case
# --------------------------------------------
# 1) Open browser (Chrome/Firefox/Edge)
# 2) Open url (https://opensource-demo.orangehrmlive.com/)
# 3) Provide Username (Admin)
# 4) Provide password (admin123)
# 5) Click on Login
# 6) Capture title of the Dashboard Page (Actual Title)
# 7) Verify title of the page: "OrangeHRM" (Expected)
# 8) Close browser

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME,"username").send_keys("Admin")

driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,"//button[@type='submit']").click()
act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()



