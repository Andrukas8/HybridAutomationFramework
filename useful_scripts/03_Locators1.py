from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()
#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg")
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
driver.close()