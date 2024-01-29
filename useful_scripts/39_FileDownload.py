from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()

def chrome_setup():
    preferences = {"download.default_directory": location}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)

    return driver

def edge_setup():
    preferences = {"download.default_directory": location}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-notifications")
    driver = webdriver.Edge(options=options)
    return driver

def firefox_setup():
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    # Mime-types for files: https://www.sitepoint.com/mime-types-complete-list/

    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2)
    # 0 - desktop
    # 1 - default location (default)
    # 2 - desired location (specified in next statement)
    ops.set_preference("browser.download.dir", location)

    driver = webdriver.Firefox(options=ops)
    return driver

# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]").click()
driver.find_element(By.XPATH, "//a[@type='button']").click()


