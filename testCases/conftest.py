from selenium import webdriver
import pytest

@pytest.fixture()
def setup():      
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)    
    return driver