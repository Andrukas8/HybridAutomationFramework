from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on the link
driver.find_element(By.LINK_TEXT,"Digital downloads").click()

# find number of links in a page
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    print(link.text)
