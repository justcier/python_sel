import logging

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import allure


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.my_account_href_xpath = "//a[text()='My account']"
        self.logger = logging.getLogger(__name__)

    @allure.step("Go to my account page")
    def go_to_my_account_page(self):
        self.logger.info("Go to my account page")
        self.driver.find_element(By.XPATH, self.my_account_href_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="my_account_page", attachment_type=AttachmentType.PNG)
