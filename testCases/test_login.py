import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()   # it will return logger method and i am saving it in a variable called logger


    def test_login(self,setup):
        self.logger.info("***** Verifying Login *****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)   # we have passed self.driver here because constructor in Login Class need this driver parameter And when I have created object of the Login class constructor automatically invokes
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)

        if act_title=="Voiceoc | Login":
            assert True
            self.driver.close()
            self.logger.info("***** Login Passed *****")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("***** Login Failed *****")
            assert False



