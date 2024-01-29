from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)


# Need to open the registration link in a new tab
# Method 1
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT, "Register").send_keys(Keys.CONTROL + Keys.RETURN)

# Method 2
driver.get("https://opencart.com/")
driver.switch_to.new_window('tab') # opens in new tab. 'window' - opens in new window
driver.get("https://orangehrm.com/")
