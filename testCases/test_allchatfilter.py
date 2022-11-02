import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from pageObjects.AllChatFilter import ChatFilter

class Test_002_Allchatfilter:
    baseURL = ReadConfig.getApplicationURL()  # using classname we directly called methods from ReadConfig because they are static methods in under ReadConfig Class
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()  # it will return logger method and i am saving it in a variable called logger

    def test_newestfilter(self,setup):

        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)  # we have passed self.driver here because constructor in Login Class need this driver parameter And when I have created object of the Login class constructor automatically invokes
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(5)

        self.logger.info("***** Verifying newest filter *****")

        self.ch = ChatFilter(self.driver)
        self.ch.newestFilter()
        self.logger.info("***** newest filter passed *****")

        self.driver.close()




    def test_azfilter(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)  # we have passed self.driver here because constructor in Login Class need this driver parameter And when I have created object of the Login class constructor automatically invokes
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(5)

        self.logger.info("***** Verifying az filter *****")
        self.ch = ChatFilter(self.driver)
        self.ch.azFilter()
        self.logger.info("***** az filter passed *****")

        self.driver.close()



    def test_zafilter(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)  # we have passed self.driver here because constructor in Login Class need this driver parameter And when I have created object of the Login class constructor automatically invokes
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.maximize_window()
        time.sleep(5)

        self.logger.info("***** Verifying za filter *****")
        self.ch = ChatFilter(self.driver)
        self.ch.zaFilter()
        self.logger.info("***** za filter passed *****")

        self.driver.close()










