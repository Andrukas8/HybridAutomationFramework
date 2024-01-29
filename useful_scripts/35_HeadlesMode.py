from selenium import webdriver

def headless_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver

def headless_edge():
    options = webdriver.EdgeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Edge(options=options)
    return driver

def headless_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(options=options)
    return driver

#driver = headless_chrome()
#driver = headless_edge()
driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.quit()