import time
import pytest
from selenium.webdriver import ActionChains

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AllChatIButton import AllChatIButton

class Test_005_AllChatIButton:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()


    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger

    def test_allchatibutton(self,setup):
        self.logger.info("***** Test_005_AllChatIButton *****")


        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(4)

        aci = AllChatIButton(self.driver)
        status = aci.ibutton()
        print(status)
        if status==True:
            assert True
            self.logger.info("***** test_AllchatIbutton passed *****")
            self.driver.close()
        else:
            self.driver.close()
            self.logger.error("***** test_AllchatIbutton failed *****")
            assert False


