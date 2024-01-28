from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SearchCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "/html[1]/body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]"

    txtEmail_xpath = "//*[@id='SearchEmail']"
    txtFName_xpath = "//*[@id='SearchFirstName']"
    txtLName_xpath = "//*[@id='SearchLastName']"

    btnSearch_xpath = "//button[@id='search-customers']"

    tblSearchResults_xpatth = "//*[@id='customers-grid_wrapper']"

    # 11 05
    drpbx_MonthDOB_xpath = "//*[@id='SearchMonthOfBirth']"
    drpbx_DayDOB_xpath = "//*[@id='SearchDayOfBirth']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(
            By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(
            By.XPATH, self.lnkCustomers_menuitem_xpath).click()

    # email
    def setSearchEmail(self, searchEmail):
        self.driver.find_element(
            By.XPATH, self.txtEmail_xpath).send_keys(searchEmail)

    def clearEmailTextBox(self):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()

    # Fname

    def setSearchFName(self, searchFName):
        self.driver.find_element(
            By.XPATH, self.txtFName_xpath).send_keys(searchFName)

    def clearSearchFNameTextBox(self):
        self.driver.find_element(By.XPATH, self.txtFName_xpath).clear()

    # Lname
    def setSearchLName(self, searchLName):
        self.driver.find_element(
            By.XPATH, self.txtLName_xpath).send_keys(searchLName)

    def clearSearchLNameTextBox(self):
        self.driver.find_element(By.XPATH, self.txtLName_xpath).clear()

    # Month dob
    def setSearchMonth(self, searchMonth):
        select = Select(self.driver.find_element(
            By.XPATH, self.drpbx_MonthDOB_xpath))
        select.select_by_value(searchMonth)

    def clearSearchMonth(self):
        select = Select(self.driver.find_element(
            By.XPATH, self.drpbx_MonthDOB_xpath))
        select.select_by_value('0')

      # Day dob
    def setSearchDay(self, searchDay):
        select = Select(self.driver.find_element(
            By.XPATH, self.drpbx_DayDOB_xpath))
        select.select_by_value(searchDay)

    def clearSearchDay(self):
        select = Select(self.driver.find_element(
            By.XPATH, self.drpbx_DayDOB_xpath))
        select.select_by_value('0')

    # #########
    def clickOnSearchButton(self):
        self.driver.find_element(By.XPATH, self.btnSearch_xpath).click()

    def getSearchResultsTable(self):
        return self.driver.find_element(By.XPATH, self.tblSearchResults_xpatth).text
