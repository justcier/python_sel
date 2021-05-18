import logging

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
import allure


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_href_xpath = "//a[text()='Cart']"
        self.empty_cart_msg_xpath = "//p[@class='cart-empty woocommerce-info']"
        self.cart_icon_xpath = "//ul[@class='site-header-cart menu']"
        self.logger = logging.getLogger(__name__)

    @allure.step("Go to cart by tab")
    def go_to_cart(self):
        self.logger.info("Go to cart by tab")
        self.driver.find_element(By.XPATH, self.cart_href_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart", attachment_type=AttachmentType.PNG)

    @allure.step("Check empty cart validation message")
    def empty_cart_validation_msg(self):
        empty_cart_validation_msg = self.driver.find_element_by_xpath(self.empty_cart_msg_xpath).text
        self.logger.info(f"Visible validation message: {empty_cart_validation_msg}")
        allure.attach(self.driver.get_screenshot_as_png(), name="empty_cart_msg", attachment_type=AttachmentType.PNG)
        return empty_cart_validation_msg

    def go_to_cart_by_icon(self):
        self.logger.info("Go to cart by icon")
        self.driver.find_element(By.XPATH, self.cart_icon_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart", attachment_type=AttachmentType.PNG)