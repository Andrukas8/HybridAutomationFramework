from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from the browser
cookies = driver.get_cookies()
print(f"Number of cookies: {len(cookies)}")

# Print details of all cookies
for c in cookies:
    #print(c) # Prints all cookies
    print(f"name = {c.get('name')} value = {c.get('value')}") # Prints names and values of the cookies

# Add new cookie to the browser to check if application allows
driver.add_cookie({"name":"MyCookie","value":"123456"})

# Printing cookies after adding the new one
cookies = driver.get_cookies()
print(f"Number of cookies: {len(cookies)}")
for c in cookies:
    print(c)

# Deleting the cookie from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print(f"Number of cookies after deleting 1: {len(cookies)}")

# Delete all cookies from the browser
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(f"Number of cookies after deleting all: {len(cookies)}")

driver.quit()