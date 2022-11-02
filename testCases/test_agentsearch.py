import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AgentSearch import AgentSearch

class Test_006_AgentSearch:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()


    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger

    def test_agent_searchByName(self,setup):
        self.logger.info("***** Test_006_AgentSearch *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()

        ass = AgentSearch(self.driver)
        time.sleep(3)

        ass.setName("Gaurav Singh")
        time.sleep(2)

        status = ass.searchByName("Gaurav Singh")
        if status == True:
            assert True
            self.logger.info("***** test_Agent_searchByName passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_Agent_searchByName failed *****")
            assert False


    def test_agent_searchByEmailid(self,setup):
        self.logger.info("***** Test_006_AgentSearch *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()

        ass = AgentSearch(self.driver)
        time.sleep(3)

        ass.setEmailId("gsingh@voiceoc.com")
        time.sleep(2)

        status = ass.searchByEmailid("gsingh@voiceoc.com")
        if status == True:
            assert True
            self.logger.info("***** test_Agent_searchByEmailID passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_Agent_searchByEmailID failed *****")
            assert False
