from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input#small-searchterms").send_keys("hello")
