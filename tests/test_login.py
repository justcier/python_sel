from datetime import datetime

import pytest
from assertpy import assert_that

import config
import data

from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage
import allure


@pytest.mark.usefixtures("browser")
class TestLogin:

    @allure.title("Login user with invalid email")
    @allure.description(f"Test login to user with invalid credentials-> email: {config.USER_WRONG_EMAIL}, "
                        f"password: {config.USER_PASSWORD}")
    @allure.testcase("https://jciercompany.qatouch.com/case/view/p/Jn3a/cid/d9med",
                     "TC0022 - Login user with invalid data")
    def test_login_with_invalid_email(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        account_page.log_in_user(config.USER_WRONG_EMAIL, config.USER_PASSWORD)
        email_validation_msg = account_page.validation_msg()
        assert_that(email_validation_msg).is_equal_to(data.ERROR_INVALID_EMAIL_LOG)

    @allure.title("Login user with valid email")
    @allure.description(f"Test login to user with valid credentials-> email: {config.USER_EMAIL}, "
                        f"password: {config.USER_PASSWORD}")
    @allure.testcase("https://jciercompany.qatouch.com/case/view/p/Jn3a/cid/xa8rr",
                     "TC0023 - Login user with valid data")
    def test_login_with_valid_credits(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        account_page.log_in_user(config.USER_EMAIL, config.USER_PASSWORD)
        account_page.is_logout_link_displayed()
