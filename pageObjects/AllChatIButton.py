import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class AllChatIButton:
    btn_ibutton_xpath = "//td[@class='w-1']//i[@xpath='1']"


    def __init__(self,driver):
        self.driver = driver

    def ibutton(self):
        flag=False
        try:
            act = ActionChains(self.driver)
            min_slider = self.driver.find_element(By.XPATH, "//div[@class='form-group']/label")
            print(min_slider.location)
            act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
            self.driver.find_element(By.XPATH, "//td[@class='w-1']/a/i").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//td[@class='w-1']/a/i").click()
            time.sleep(3)
            flag=True
        except:
            flag=False

        return flag

