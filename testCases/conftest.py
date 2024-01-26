from selenium import webdriver
import pytest
from utilities.customLogger import LogGen

logger = LogGen.loggen()


@pytest.fixture()
def setup(browser):
    if browser:
        browser = browser.lower()
    else:
        browser = 'chrome'
    
    if browser not in ("chrome","firefox","edge","safari"):
        browser = 'chrome'

    infoMsg = f"********** Launching {browser} browser..."
    logger.info(infoMsg)
    print(infoMsg)

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'edge':
        driver = webdriver.Edge()

    elif browser == 'safari':
        driver = webdriver.Safari()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
