import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # Test Data
    email = "victoria_victoria@nopCommerce.com"
    fName = "James"
    lName = "Gates"
    dobMonth = "11"
    dobDay = "5"

    def test_SearchCustomer(self, setup):
        self.logger.info("********** Test_004_SearchCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Succesful")

        self.logger.info("***** Starting Search Customer Test")

        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.clickOnCustomersMenu()
        self.searchcust.clickOnCustomersMenuItem()

        # Search By Email
        if self.email:
            self.logger.info("*** Starting Search Customer By Email Test...")
            self.searchcust.clearEmailTextBox()
            self.searchcust.setSearchEmail(self.email)
            self.searchcust.clickOnSearchButton()
            time.sleep(3)
            searchResults = self.searchcust.getSearchResultsTable()
            self.searchcust.clearEmailTextBox()

            if self.email in searchResults:
                assert True == True
                self.logger.info("*** Search customer by Email Passed")
            else:
                assert True == False
                self.logger.info("*** Search Customer by Email Failed")

            self.logger.info("*** Finished Search Customer By Email Test...")

        # Search By FName
        if self.fName:
            self.logger.info(
                "*** Starting Search Customer By First Name Test...")
            self.searchcust.clearSearchFNameTextBox()
            self.searchcust.setSearchFName(self.fName)
            self.searchcust.clickOnSearchButton()
            time.sleep(3)
            searchResults = self.searchcust.getSearchResultsTable()

            self.searchcust.clearSearchFNameTextBox()

            if self.fName in searchResults:
                assert True == True
                self.logger.info("*** Search customer by First Name Passed")
            else:
                assert True == False
                self.logger.info("*** Search Customer by First Name Failed")

            self.logger.info(
                "*** Finished Search Customer By First Name Test...")

        # Search By LName
        if self.lName:
            self.logger.info(
                "*** Starting Search Customer By Last Name Test...")
            self.searchcust.clearSearchLNameTextBox()
            self.searchcust.setSearchLName(self.lName)
            self.searchcust.clickOnSearchButton()
            time.sleep(3)
            searchResults = self.searchcust.getSearchResultsTable()

            self.searchcust.clearSearchLNameTextBox()

            if self.lName in searchResults:
                assert True == True
                self.logger.info("*** Search customer by Last Name Passed")
            else:
                assert True == False
                self.logger.info("*** Search Customer by Last Name Failed")

            self.logger.info(
                "*** Finished Search Customer By Last Name Test...")

        # Search By Month DOB
        if self.dobMonth:
            self.logger.info(
                "*** Starting Search Customer By DOB Month Test...")
            self.searchcust.clearSearchMonth()
            self.searchcust.setSearchMonth(self.dobMonth)
            self.searchcust.clickOnSearchButton()
            time.sleep(3)
            searchResults = self.searchcust.getSearchResultsTable()

            self.searchcust.clearSearchMonth()

            if "No data available in table" not in searchResults:
                assert True == True
                self.logger.info("*** Search customer by DOB Month Passed")
            else:
                assert True == False
                self.logger.info("*** Search Customer by DOB Month Failed")

            self.logger.info(
                "*** Finished Search Customer By DOB Month Test...")

       # Search By Day DOB
        if self.dobDay:
            self.logger.info("*** Starting Search Customer By DOB Day Test...")
            self.searchcust.clearSearchDay()
            self.searchcust.setSearchDay(self.dobDay)
            self.searchcust.clickOnSearchButton()
            time.sleep(3)
            searchResults = self.searchcust.getSearchResultsTable()

            self.searchcust.clearSearchDay()

            if "No data available in table" not in searchResults:
                assert True == True
                self.logger.info("*** Search customer by DOB Day Passed")
            else:
                assert True == False
                self.logger.info("*** Search Customer by DOB Day Failed")

            self.logger.info("*** Finished Search Customer By DOB Day Test...")

        #####
        self.driver.quit()
