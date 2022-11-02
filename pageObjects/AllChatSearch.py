from selenium.webdriver.common.by import By

class AllChatSearch:
    txt_allchatsearch_xpath = "//input[@name='search']"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//div[@class='table-responsive']"
    tableRows_xpath = "//div[@class='table-responsive']//tbody/tr"
    tableColumns_xpath = "//div[@class='table-responsive']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.txt_allchatsearch_xpath).send_keys(name)

    def setContext(self, context):
        self.driver.find_element(By.XPATH, self.txt_allchatsearch_xpath).send_keys(context)

    def setMobielNo(self, mobileno):
        self.driver.find_element(By.XPATH, self.txt_allchatsearch_xpath).send_keys(mobileno)

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
            contextt = table.find_element(By.XPATH,"//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[6]").text
            if context == contextt:
                flag = True
                break

        return flag

    def searchByMobileNo(self, mobileno):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            mobilenoo = table.find_element(By.XPATH,"//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[5]").text
            if mobileno == mobilenoo:
                flag = True
                break

        return flag



