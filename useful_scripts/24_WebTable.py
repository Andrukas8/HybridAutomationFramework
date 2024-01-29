from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count number of rows and columns in the table
no0Rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
no0Cols = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/th"))
print(f"Rows {no0Rows}, Columns {no0Cols}")

# Read specific row and column data
data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[5]/td[1]").text
print(f"Data = {data}")

# Read all rows and all columns
for i in range(2,no0Rows+1):
    for j in range(1,no0Cols+1):
        print(driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{i}]/td[{j}]").text + " ", end="")
    print()

# Get books writen by specific author
for i in range(2,no0Rows):
    author = driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{i}]/td[2]").text
    if author == "Mukesh":
        print(driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{i}]/td[1]").text)


driver.quit()