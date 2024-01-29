import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    
    @pytest.mark.sanity    
    def test_addCustomer(self, setup):
        self.logger.info("********** Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*** Login Succesful")
        
        self.logger.info("***** Starting Add Customer Test")
        
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()
        
        self.logger.info("***** Providing Customer Info")        
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Vasyl")
        self.addcust.setLastName("Mikitenko")
        self.addcust.setCompanyName("busyQA")                      
        self.addcust.setAdminContent("This is for testing")
        self.addcust.setDob("1/09/1987")
        self.addcust.setGender("Female")        
        self.addcust.setCustomerRoles("Guests")        
        self.addcust.setManagerOfVendor("Vendor 2")
                        
        self.addcust.setTaxExempt()
        self.addcust.clickOnSave()
        
        self.logger.info("***** Saving customer info")
        self.logger.info("***** Add customer validation")
        
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text # capturing everrything on the page
        
        if 'customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*** Add Customer Test Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_addCustomer_scr.png") # adding Screenshots
            assert True == False
            self.logger.error("***** Add Customer Test Failed")
        
        self.driver.close()
        self.logger.info("********** Ending Add Customer Test ")
        
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))