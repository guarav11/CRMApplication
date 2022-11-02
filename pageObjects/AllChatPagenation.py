from selenium import webdriver
from selenium.webdriver.common.by import By


class AllChatPagenation:
    arrow_right_pagenation_xpath = "//div[@class='selectgroup align-to-right paginations']/i[2]"
    arrow_left_pagenation_xpath = "//div[@class='selectgroup align-to-right paginations']/i[1]"
    no_xpath = "//div[@class='selectgroup align-to-right paginations']/span"

    def __init__(self, driver):
        self.driver = driver

    def rightpagenation(self):
        self.driver.find_element(By.XPATH, self.arrow_right_pagenation_xpath).click()
        pserail_no = self.driver.find_element(By.XPATH, self.no_xpath).text
        dt = pserail_no.split("-")
        print(dt)
        flag = False
        for r in dt:
            # print(r)
            d = str(11)
            if r==d:
                print(r)
                print(d)
                flag = True
            else:
                flag = False
            break

        return flag




    def leftpagenation(self):
        button = self.driver.find_element(By.XPATH, self.arrow_left_pagenation_xpath)
        while True:
            try:
                button.Click()
            except:
                break
