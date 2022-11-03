import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class LeadDashboard:
    link_leaddashboard_xpath = "//a[normalize-space()='Lead Dashboard']"
    txt_searchbox_xpath = "//input[@placeholder='Search']"
    btn_submit_xpath = "//body[1]/span[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/button[1]"

    table_xpath = "//div[@class='table-responsive']"
    tableRows_xpath = "//div[@class='table-responsive']//tbody/tr"
    tableColumns_xpath = "//div[@class='table-responsive']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def setContext(self, context):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(context)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def setMobielNo(self, mobileno):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(mobileno)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def setdate(self, date):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(date)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def settime(self, time):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(time)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def setpurpose(self, purpose):
        self.driver.find_element(By.XPATH, self.link_leaddashboard_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_searchbox_xpath).send_keys(purpose)
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchByName(self, name):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            namme = table.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == namme:
                flag = True
                break

        return flag

    def searchByContext(self, context):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            contextt = table.find_element(By.XPATH,
                                          "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[5]").text
            if context == contextt:
                flag = True
                break

        return flag

    def searchByMobileNo(self, mobileno):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            mobilenoo = table.find_element(By.XPATH,
                                           "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[2]").text
            if mobileno == mobilenoo:
                flag = True
                break

        return flag

    def searchByBookingDate(self, date):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            dates = table.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[6]").text
            if date == dates:
                flag = True
                break

        return flag

    def searchByBookingTime(self, time):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            times = table.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[7]").text
            if time == times:
                flag = True
                break

        return flag

    def searchByPurpose(self, purpose):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            purposes = table.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[9]").text
            if purpose == purposes:
                flag = True
                break

        return flag



