import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class EditAgent:
    link_agents_xpath = "//a[normalize-space()='Agents']"
    link_addnewagent_xpath = "//a[normalize-space()='Add New Agent']"
    txt_agentname_xpath = "//input[@placeholder='Agent Name']"
    txt_agentemailid_xpath = "//input[@placeholder='Email ID']"
    txt_agenteditemailid_xpath = "//input[@placeholder='Email Id']"
    txt_agentid_xpath = "//input[@placeholder='Agent Id']"
    chkbox_agenttype_xpath = "//input[@value='chatAgent']"
    chkbox_agentypelead_xpath = "//input[@value='leadAgent']"
    btn_createbutton_xpath = "//button[normalize-space()='Create']"

    link_viewagent_xpath = "//a[normalize-space()='View Agents']"
    link_editagent_xpath = "//a[@title='Click to edit']"
    btn_updateagent_xpath = "//button[normalize-space()='Update']"
    al_addagentsuccessmessage_xpath = "//div[@role='alert']"

    link_deleteagent_xpath = "//a[@title='Click to delete']"

    link_banagent_xpath = "//a[@title='Click to ban']"
    link_unbanagent_xpath = "//a[@title='Click to unblock']"


    def __init__(self,driver):
        self.driver = driver


    def createagent(self):
        self.driver.find_element(By.XPATH, self.link_agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_addnewagent_xpath).click()

        self.driver.find_element(By.XPATH, self.txt_agentname_xpath).send_keys("Gaurav Singh")
        self.driver.find_element(By.XPATH, self.txt_agentemailid_xpath).send_keys("gsingh@voiceoc.com")
        self.driver.find_element(By.XPATH, self.txt_agentid_xpath).send_keys(100)
        self.driver.find_element(By.XPATH, self.chkbox_agenttype_xpath).click()

        self.driver.find_element(By.XPATH, self.btn_createbutton_xpath).click()
        time.sleep(1)

        message = self.driver.find_element(By.XPATH, self.al_addagentsuccessmessage_xpath).text
        print(message)
        return message

    def banagent(self):
        self.driver.find_element(By.XPATH, self.link_agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link_banagent_xpath).click()
        time.sleep(1)

        message = self.driver.find_element(By.XPATH, self.al_addagentsuccessmessage_xpath).text
        print(message)
        return message

    def unbanagent(self):
        self.driver.find_element(By.XPATH, self.link_agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link_unbanagent_xpath).click()
        time.sleep(1)

        message = self.driver.find_element(By.XPATH, self.al_addagentsuccessmessage_xpath).text
        print(message)
        return message


    def editagentdetails(self):
        self.driver.find_element(By.XPATH, self.link_agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link_editagent_xpath).click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.txt_agentname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_agentname_xpath).send_keys("Gaurav")
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.txt_agenteditemailid_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_agenteditemailid_xpath).send_keys("gsingh@gmail.com")
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.txt_agentid_xpath).clear()
        self.driver.find_element(By.XPATH, self.txt_agentid_xpath).send_keys(101)
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.chkbox_agentypelead_xpath).click()

        self.driver.find_element(By.XPATH, self.btn_updateagent_xpath).click()
        time.sleep(1)

        message = self.driver.find_element(By.XPATH, self.al_addagentsuccessmessage_xpath).text
        print(message)
        return message

    def deleteagent(self):
        self.driver.find_element(By.XPATH, self.link_agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.link_deleteagent_xpath).click()
        time.sleep(1)

        self.driver.switch_to.alert.accept()
        time.sleep(1)

        message = self.driver.find_element(By.XPATH, self.al_addagentsuccessmessage_xpath).text
        print(message)
        return message


