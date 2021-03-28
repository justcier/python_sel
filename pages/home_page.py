from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import selenium

from common.base_page import BasePage
from common.locators import Locator


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_href_xpath = "//a[text()='My account']"

    def go_to_my_account_page(self):
        self.driver.find_element_by_xpath(self.my_account_href_xpath).click()

    #  MY_ACCOUNT_LINK = Locator(
    #     location="//a[text()='My account']",
    #     method=By.XPATH
    # )

    #  MY_ACCOUNT_LINK = driver.find_element_by_xpath("//a[text()='My account']").click()

    # def go_to_my_account_page(self):
    #     self.find_clickable_element(self.MY_ACCOUNT_LINK).click()
