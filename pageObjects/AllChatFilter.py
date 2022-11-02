from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ChatFilter:
    drp_filter_xpath = "//*[@id='root']/div/div/div[3]/div/div/div[1]/div/div/div[1]/select"
    table_xpath = "//div[@class='table-responsive']"

    def __init__(self,driver):
        self.driver = driver

    def newestFilter(self):

        self.filter = Select(self.driver.find_element(By.XPATH, self.drp_filter_xpath))
        self.filter.select_by_value("latest")


        # try:
        #     table_id = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))
        #     rows = table_id.find_elements(By.TAG_NAME, "tr")
        #     for row in rows:
        #         # Get the columns
        #         col_name = row.find_elements(By.TAG_NAME, "td")[1]  # This is the Configuration Name column
        #         col_name.is_column_sorted
        #         col_type = row.find_elements(By.TAG_NAME, "td")[3]  # This is the Type column
        #         col_rows = row.find_elements(By.TAG_NAME, "td")[4]  # This is the Rows column
        #         print("col_name.text = ")
        #         print(col_name.text)
        #         print(col_type.text)
        #         print(col_rows.text)
        #         if (col_name.text == "data1"):
        #             return True
        #     return False
        # except NoSuchElementException:
        #     print("Element not found ")
        #     return False





    def azFilter(self):
        self.filter = Select(self.driver.find_element(By.XPATH, self.drp_filter_xpath))
        self.filter.select_by_visible_text("Name (A - Z)")

    def zaFilter(self):
        self.filter = Select(self.driver.find_element(By.XPATH, self.drp_filter_xpath))
        self.filter.select_by_visible_text("Name (Z - A)")


