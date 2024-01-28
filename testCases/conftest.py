from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
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
    
    driver.implicitly_wait(10)
    
    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Generating PyTest HTML Report ##########

# Hook for adding environment info to the HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:        
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Andriy'

# Hook for deletting/modifying Environment info of the HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
