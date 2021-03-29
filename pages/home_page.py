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
        self.driver.find_element(By.XPATH, self.my_account_href_xpath).click()
