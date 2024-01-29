from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry_ele = driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry = Select(drpcountry_ele)

drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("10")
#drpcountry.select_by_index(13)

# capture all the options and print them
options = drpcountry.options
print(len(options))

for opt in options:
    print(opt.text)

# Select option from dropdown without using built-in method
for opt in options:
    if opt.text == "India":
        opt.click()
        break
