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
        self.cart_href_xpath = "//a[text()='Cart']"
        self.cart_icon_xpath = "//ul[@class='site-header-cart menu']"
        # self.add_to_cart_button_xpath = \
        #     f"//h2[text()={}]/parent::*/parent::*//a[contains(@class,'button product_type_simple')]"
        # self.album_view_cart_button_xpath = \
        #     f"//h2[text()={}]/parent::*/parent::*//a[contains(@class,'added_to_cart wc-forward')]"
        self.album_add_to_cart_button_xpath = \
            "//h2[text()='Album']/parent::*/parent::*//a[contains(@class,'button product_type_simple')]"
        self.album_view_cart_button_xpath = \
            "//h2[text()='Album']/parent::*/parent::*//a[contains(@class,'added_to_cart wc-forward')]"
        self.logger = logging.getLogger(__name__)

    @allure.step("Go to my account page")
    def go_to_my_account_page(self):
        self.logger.info("Go to my account page")
        self.driver.find_element(By.XPATH, self.my_account_href_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="my_account_page", attachment_type=AttachmentType.PNG)

    @allure.step("Go to cart by tab")
    def go_to_cart(self):
        self.logger.info("Go to cart by tab")
        self.driver.find_element(By.XPATH, self.cart_href_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart", attachment_type=AttachmentType.PNG)

    @allure.step("Go to cart by icon")
    def go_to_cart_by_icon(self):
        self.logger.info("Go to cart by icon")
        self.driver.find_element(By.XPATH, self.cart_icon_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="cart", attachment_type=AttachmentType.PNG)

    @allure.step("Click add to cart button")
    def click_add_to_cart_button(self, product_name):
        self.logger.info(f"Click add button for {product_name})")
        selector = f"//h2[text()='{product_name}']/parent::*/parent::*//a[contains(@class,'button product_type_simple')]"
        self.driver.find_element(By.XPATH, selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="click_add_button", attachment_type=AttachmentType.PNG)

    @allure.step("Click View cart button")
    def click_view_cart_button(self, product_name):
        self.logger.info(f"Click view cart under {product_name})")
        selector = f"//h2[text()='{product_name}']/parent::*/parent::*//a[contains(@class,'added_to_cart wc-forward')]"
        self.driver.find_element(By.XPATH, selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="click view cart", attachment_type=AttachmentType.PNG)
