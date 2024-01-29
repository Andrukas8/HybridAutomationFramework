from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_ele = driver.find_element(By.ID, "box6")
target_ele = driver.find_element(By.ID, "box106")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box3")
target_ele = driver.find_element(By.ID, "box103")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box1")
target_ele = driver.find_element(By.ID, "box101")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box2")
target_ele = driver.find_element(By.ID, "box102")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box4")
target_ele = driver.find_element(By.ID, "box104")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box5")
target_ele = driver.find_element(By.ID, "box105")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()

source_ele = driver.find_element(By.ID, "box7")
target_ele = driver.find_element(By.ID, "box107")
act = ActionChains(driver)
act.drag_and_drop(source_ele,target_ele).perform()