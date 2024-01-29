from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
# mm/dd/yyy
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("05/30/2022")
year="2025"
month="March"
date="30"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//a[@title='Next']").click()


dates = driver.find_elements(By.XPATH,"/html/body/div/table/tbody/tr/td/a")

for ele in dates:
    print(ele.text)
    if ele.text == date:
        ele.click()
        break