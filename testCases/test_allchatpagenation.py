import time
import pytest
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AllChatPagenation import AllChatPagenation

class Test_004_AllChatPagenation:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()


    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger

    def test_allchatrightpagenation(self,setup):
        self.logger.info("***** Test_004_AllChatPagenation *****")


        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(6)

        acp = AllChatPagenation(self.driver)
        status = acp.rightpagenation()
        if status==True:
            assert True
            self.logger.info("***** test_Allchatrightpagenation passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_Allchatrightpagenation failed *****")
            assert False



    def test_allchatleftpagenation(self, setup):
        self.logger.info("***** Test_004_AllChatPagenation *****")


        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(6)

        acp = AllChatPagenation(self.driver)
        acp.leftpagenation()

        self.logger.info("***** test_Allchatleftpagenation passed *****")

        self.driver.close()

