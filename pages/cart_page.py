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
        self.empty_cart_msg_xpath = "//p[@class='cart-empty woocommerce-info']"
        self.checkout_button_xpath = "//a[@class='checkout-button button alt wc-forward']"
        self.logger = logging.getLogger(__name__)

    @allure.step("Check empty cart message")
    def empty_cart_msg(self):
        empty_cart_msg = self.driver.find_element_by_xpath(self.empty_cart_msg_xpath).text
        self.logger.info(f"Visible validation message: {empty_cart_msg}")
        allure.attach(self.driver.get_screenshot_as_png(), name="empty_cart_msg", attachment_type=AttachmentType.PNG)
        return empty_cart_msg

    @allure.step("Text on checkout button")
    def text_on_checkout_button(self):
        checkout_button_text = self.driver.find_element(By.XPATH, self.checkout_button_xpath).text
        self.logger.info(f"User is in cart and see checkout button with text {checkout_button_text}")
        allure.attach(self.driver.get_screenshot_as_png(), name="checkout_button", attachment_type=AttachmentType.PNG)
        return checkout_button_text
