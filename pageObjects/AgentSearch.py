from selenium.webdriver.common.by import By

class AgentSearch:
    link_Agents_xpath = "//a[normalize-space()='Agents']"
    link_viewagent_xpath = "//a[normalize-space()='View Agents']"
    txt_search_xpath = "//input[@name='search']"
    btn_go_xpath = "//button[normalize-space()='Go!']"


    table_xpath = "//table[@class='table card-table table-striped table-vcenter table-hover']"
    tableRows_xpath = "//table[@class='table card-table table-striped table-vcenter table-hover']//tbody/tr"
    tableColumns_xpath = "//table[@class='table card-table table-striped table-vcenter table-hover']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.link_Agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_search_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.btn_go_xpath).click()

    def setEmailId(self, emailid):
        self.driver.find_element(By.XPATH, self.link_Agents_xpath).click()
        self.driver.find_element(By.XPATH, self.link_viewagent_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_search_xpath).send_keys(emailid)
        self.driver.find_element(By.XPATH, self.btn_go_xpath).click()

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

    def searchByEmailid(self, emailid):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailidd = table.find_element(By.XPATH, "//div[@class='table-responsive']//tbody/tr[" + str(r) + "]/td[4]").text
            if emailid == emailidd:
                flag = True
                break

        return flag
