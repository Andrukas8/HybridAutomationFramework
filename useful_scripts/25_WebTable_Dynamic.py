from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Admin --> User Management --> Users
driver.find_element(By.XPATH,"//a[@href='/web/index.php/admin/viewAdminModule']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()

numRows = len(driver.find_elements(By.XPATH,"//div[@role='row']"))
sampleText = driver.find_elements(By.XPATH,"//div[@role='row'][1]")
print(f"Number of rows = {numRows}")
print(f"Sample text = {sampleText[2].text}")
