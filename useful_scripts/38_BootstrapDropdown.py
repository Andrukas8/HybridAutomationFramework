from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countrieslist = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for country in countrieslist:
    if country.text == "India":
        country.click()
        break
