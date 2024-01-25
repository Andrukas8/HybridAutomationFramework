import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("***** Verifying Homepage Title")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Homepage Title test Passed")
        else:
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Homepage Title test Failed")
            assert False

    def test_login(self, setup):
        self.logger.info("***** Verifying Login test")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("Login test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("Login test Failed")
            assert False
