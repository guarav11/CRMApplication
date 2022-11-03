import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LeadDashboard import LeadDashboard

class Test_008_LeadDashboard:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()


    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger

    def test_searchByName(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.setName("Gaurrav Singh")
        time.sleep(3)

        status = acs.searchByName("Gaurrav Singh")
        if status==True:
            assert True
            self.logger.info("***** test_searchByName passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchByName failed *****")
            assert False

    def test_searchByContext(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.setContext("checkout_report")
        time.sleep(3)

        status = acs.searchByContext("checkout_report")
        if status==True:
            assert True
            self.logger.info("***** test_searchByContext passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchByContext failed *****")
            assert False


    def test_searchByMobileNo(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.setMobielNo("918467036799")
        time.sleep(3)

        status = acs.searchByMobileNo("918467036799")
        if status==True:
            assert True
            self.logger.info("***** test_searchByMobileNo passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchByMobileNo failed *****")
            assert False

    def test_searchByBookingdate(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.setdate("16-09-2022")
        time.sleep(3)

        status = acs.searchByBookingDate("16-09-2022")
        if status==True:
            assert True
            self.logger.info("***** test_searchByDate passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchByDate failed *****")
            assert False

    def test_searchByBookingtime(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.settime("3am")
        time.sleep(3)

        status = acs.searchByBookingTime("3am")
        if status==True:
            assert True
            self.logger.info("***** test_searchBytime passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchBytime failed *****")
            assert False

    def test_searchByPurpose(self,setup):
        self.logger.info("***** Test_008_LeadDashboard *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()


        acs = LeadDashboard(self.driver)
        time.sleep(3)

        acs.setpurpose("Lead")
        time.sleep(3)

        status = acs.searchByPurpose("Lead")
        print(status)
        if status==True:
            assert True
            self.logger.info("***** test_searchBypurose passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_searchBypurpose failed *****")
            assert False