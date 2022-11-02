import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.EditAgent import EditAgent
from selenium.webdriver.support.ui import WebDriverWait

class Test_007_EditAgent:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()


    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger


    def test_createagent(self,setup):

        self.logger.info("***** Test_007_AddNewAgent *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        ana = EditAgent(self.driver)
        message = ana.createagent()

        if message=="Agent created successfully.":
            assert True
            self.logger.info("***** test_create_agent passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_create_agent failed *****")
            assert False


    def test_banagent(self,setup):
        self.logger.info("***** Test_007_BanAgent *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        ban = EditAgent(self.driver)
        message = ban.banagent()

        if message=="Agent Blocked Successfully.":
            assert True
            self.logger.info("***** test_ban_agent passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_ban_agent failed *****")
            assert False


    def test_unbanagent(self,setup):
        self.logger.info("***** Test_007_UnbanAgent *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        unban = EditAgent(self.driver)
        message = unban.unbanagent()

        if message=="Agent Activated Successfully.":
            assert True
            self.logger.info("***** test_unban_agent passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_unban_agent failed *****")
            assert False


    def test_editagentdetails(self,setup):
        self.logger.info("***** Test_007_EditAgent *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        anaa = EditAgent(self.driver)
        message = anaa.editagentdetails()

        if message=="Admin updated successfully.":
            assert True
            self.logger.info("***** test_add_agent passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_add_agent failed *****")
            assert False

    def test_deleteagent(self,setup):
        self.logger.info("***** Test_007_DeleteAgent *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(2)

        da = EditAgent(self.driver)
        message = da.deleteagent()

        if message=="Agent Deleted Successfully.":
            assert True
            self.logger.info("***** test_delete_agent passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_delete_agent failed *****")
            assert False
