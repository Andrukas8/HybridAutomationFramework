from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
min_slider = driver.find_element(By.XPATH, "//body//div//span[1]")
max_slider = driver.find_element(By.XPATH, "//body//div//span[2]")

print("Location of Sliders Before Moving...")
print(f"min = {min_slider.location}, max = {max_slider.location}")
# min = {'x': 59, 'y': 251}
# max = {'x': 766, 'y': 251}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,20,0).perform()
act.drag_and_drop_by_offset(max_slider,-20,0).perform()

print("Location of Sliders After Moving...")
print(f"min = {min_slider.location}, max = {max_slider.location}")

# min = {'x': 81, 'y': 251} # exact numbers should not show because it depends on resolution
# max = {'x': 745, 'y': 251}