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
        # css = "a[href='http://demostore.supersqa.com/my-account/']"
        self.cart_href_xpath = "//a[text()='Cart']"  # css = "a[href='http://demostore.supersqa.com/cart/']"
        self.cart_icon_xpath = "//ul[@class='site-header-cart menu']"  # css = "ul.site-header-cart.menu"
        self.album_add_to_cart_button_xpath = (
            lambda product_name: f"//h2[text()='{product_name}']/parent::*/parent::*//a[contains(@class,'button "
                                 f"product_type_simple')]"
        )
        self.album_view_cart_button_xpath = (
            lambda product_name: f"//h2[text()='{product_name}']/parent::*/parent::*//a[contains(@class,'added_to_cart "
                                 f"wc-forward')] "
        )
        self.product_price_xpath = (
            lambda product_name: f"//h2[text()='{product_name}']//parent::*//span[@class='woocommerce-Price-amount "
                                 f"amount'] "
        )
        self.price_near_cart_icon_css = "a.cart-contents span.woocommerce-Price-amount"
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
        selector = self.album_add_to_cart_button_xpath(product_name)
        self.driver.find_element(By.XPATH, selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="click_add_button", attachment_type=AttachmentType.PNG)

    @allure.step("Click View cart button")
    def click_view_cart_button(self, product_name):
        self.logger.info(f"Click view cart under {product_name})")
        selector = self.album_view_cart_button_xpath(product_name)
        self.driver.find_element(By.XPATH, selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="click view cart", attachment_type=AttachmentType.PNG)

    def add_multiple_product(self, list_of_products):
        self.logger.info(f"Add product to cart: {list_of_products}")

        for product in list_of_products:
            self.click_add_to_cart_button(product)

    def check_price_near_cart_icon(self):
        self.logger.info(f"Check price near cart icon")
        return self.driver.find_element(By.CSS_SELECTOR, self.price_near_cart_icon_css).text

    def sum_of_added_product_to_cart(self, list_of_products):
        self.logger.info(f"Sum all products added to cart: {list_of_products}")
        value_of_products = 0.0

        for product in list_of_products:
            price = self.driver.find_element(By.XPATH, self.product_price_xpath(product)).text
            value_of_products += float(price.replace("$", ""))

        return "$" + str(value_of_products)
