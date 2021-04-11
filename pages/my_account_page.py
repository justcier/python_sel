import logging
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.register_email_input_id = "reg_email"
        self.register_password_input_id = "reg_password"
        self.register_button_css_selector = "button[name='register']"
        self.log_out_href_in_my_account_xpath = "//a[text()='Logout']"
        self.password_validation_msg_xpath = "//div[contains(@class, 'woocommerce-password-strength')]"
        self.login_email_input_id = "username"
        self.login_password_input_id = "password"
        self.login_button_css_selector = "button[name='login']"
        self.error_msg_xpath = "//ul[@class='woocommerce-error']/li"
        self.logger = logging.getLogger(__name__)

    @allure.step("Fill login form with email: '{1}' and password: '{2}'")
    def fill_login_form(self, user_email, user_password):
        self.logger.info(f"Fill login form with user email: {user_email} and user password: {user_password}")
        email_input = self.driver.find_element(By.ID, self.login_email_input_id)
        password_input = self.driver.find_element(By.ID, self.login_password_input_id)
        email_input.click()
        email_input.send_keys(user_email)
        password_input.click()
        password_input.send_keys(user_password)
        allure.attach(self.driver.get_screenshot_as_png(), name="filled_login_form", attachment_type=AttachmentType.PNG)

    @allure.step("Login with email: '{1}' and password: '{2}'")
    def log_in_user(self, user_email, user_password):
        self.logger.info(f"Login with credentials user email: {user_email} and user password: {user_password}")
        self.fill_login_form(user_email, user_password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="logged_user", attachment_type=AttachmentType.PNG)

    @allure.step("Fill register form with email: '{1}' and password: '{2}'")
    def fill_register_form(self, user_email, user_password):
        self.logger.info(f"Fill register form with user email: {user_email} and user password: {user_password}")
        email_input = self.driver.find_element(By.ID, self.register_email_input_id)
        password_input = self.driver.find_element(By.ID, self.register_password_input_id)
        email_input.click()
        email_input.send_keys(user_email)
        password_input.click()
        password_input.send_keys(user_password)
        allure.attach(self.driver.get_screenshot_as_png(), name="filled_register_form",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Register user with email: '{1}' and password: '{2}'")
    def register_user(self, user_email, user_password):
        self.logger.info(f"Register user with credentials user email: {user_email} and user password: {user_password}")
        self.fill_register_form(user_email, user_password)
        self.driver.find_element(By.CSS_SELECTOR, self.register_button_css_selector).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="registered_user", attachment_type=AttachmentType.PNG)

    @allure.step("Check if the user is correctly logged in -> logout link is displayed")
    def is_logout_link_displayed(self):
        self.logger.info("Check if the user is correctly logged in -> logout link is displayed")
        allure.attach(self.driver.get_screenshot_as_png(), name="logged_user_view", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(By.XPATH, self.log_out_href_in_my_account_xpath).is_displayed()

    @allure.step("Check validation message")
    def login_validation_msg(self, user_email, user_password):
        self.fill_login_form(user_email, user_password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()
        validation_msg = self.driver.find_element_by_xpath(self.error_msg_xpath).text
        self.logger.info(f"Check validation message: {validation_msg}")
        allure.attach(self.driver.get_screenshot_as_png(), name="validation_msg", attachment_type=AttachmentType.PNG)
        return validation_msg
