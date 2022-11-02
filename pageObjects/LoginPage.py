from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_xpath = "//input[@name='email']"
    textbox_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//button[@type='submit']"
    img_superAdmin_xpath = "//a//span[2]"
    btn_logout_xpath = "//a[normalize-space()='Sign Out']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.img_superAdmin_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()



