from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications") # disables notification popup
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,3000)","")
#value = driver.execute_script("return window.pageYOffset;")
#print(f"Number of pixels moved: {value}") # 3000

# Scroll down page till the element is visible
# ua_flag = driver.find_element(By.XPATH, "//img[@alt='Flag of Ukraine']")
# driver.execute_script("arguments[0].scrollIntoView();",ua_flag)
# value = driver.execute_script("return window.pageYOffset;")
# print(f"Number of pixels moved: {value}") # 8344

# Scroll down the page till it ends
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f"Number of pixels moved: {value}") # 9448

time.sleep(2)

# Scroll up the page to the starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print(f"Number of pixels moved: {value}") # 9448

