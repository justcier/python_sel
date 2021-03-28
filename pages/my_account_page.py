from common.base_page import BasePage


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.register_email_input_css_selector = "input[type='email']"
        self.register_password_input_css_selector = "input[id='reg_password']"
        self.register_button_css_selector = "button[name='register']"

    def register_user(self, user_email, user_password):
        email_input = self.driver.find_element_by_css_selector("input[type='email']")
        password_input = self.driver.find_element_by_css_selector("input[id='reg_password']")
        email_input.click()
        email_input.send_keys(user_email)
        password_input.click()
        password_input.send_keys(user_password)
        self.driver.find_element_by_css_selector("button[name='register']").click()
