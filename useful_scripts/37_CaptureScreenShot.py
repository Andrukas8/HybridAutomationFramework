from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Method 1
# driver.save_screenshot("C:\\Users\\andri\\PycharmProjects\\SDETQA\\day_23\\homepage.png")
# driver.save_screenshot(os.getcwd() + "\\homepage.png")

# Method 2
# driver.get_screenshot_as_png() driver.get_screenshot_as_base64()

driver.quit()


