from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick")
driver.maximize_window()


driver.find_element(By.XPATH, "//*[@id='accept-choices']").click()
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='iframeResult']"))
button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")

act = ActionChains(driver)

act.double_click(button).perform()



