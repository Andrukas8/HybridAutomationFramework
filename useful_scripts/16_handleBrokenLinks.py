from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_Links = driver.find_elements(By.TAG_NAME,"a")
count = 0

for link in all_Links:
    url = link.get_attribute("href")

    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url," is a broken link")
        count += 1
    else:
        print(url," is a valid link")

print("Total number of broken links: ",count)

driver.quit()


