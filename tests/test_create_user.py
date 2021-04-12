import pytest
from assertpy import assert_that

import config
import allure
from datetime import datetime
from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("browser")
class TestCreateUser:

    @allure.title("Create user")
    @allure.description("Test create user with valid credentials")
    @allure.testcase("https://jciercompany.qatouch.com/case/view/p/Jn3a/cid/ZaVbz",
                     "TC0021 - Create user in my account page")
    def test_create_user(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        generate_email = f"email{datetime.now().microsecond}@test.com"
        generate_password = f"password{datetime.now().microsecond}"
        home_page.go_to_my_account_page()
        account_page.register_user(generate_email, generate_password)
        account_page.is_logout_link_displayed()

    @allure.title("Create user with existing data")
    @allure.description(f"Test try to create user with existing data in database-> email: {config.USER_EMAIL} "
                        f"and password: {config.USER_PASSWORD}")
    @allure.testcase("https://jciercompany.qatouch.com/case/edit/p/Jn3a/cid/5gz9M",
                     "TC0024 - Create user in my account page with existing data")
    def test_create_user_with_existing_data(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        account_page.register_user(config.USER_EMAIL, config.USER_PASSWORD)
        error_msg = account_page.validation_msg()
        assert_that(error_msg).is_equal_to(
            'Error: An account is already registered with your email address. Please log in.')

    @allure.title("Create user with invalid email")
    @allure.description(f"Test try to create user with invalid email: a@b.c")
    @allure.testcase("https://jciercompany.qatouch.com/case/view/p/Jn3a/cid/d9N3Z",
                     "TC0025 - Create user in my account page with invalid email")
    def test_create_user_with_invalid_email(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        account_page.register_user("a@b.c", config.USER_PASSWORD)
        error_msg = account_page.validation_msg()
        assert_that(error_msg).is_equal_to('Error: Please provide a valid email address.')

    @allure.title("Test param create user validation")
    @pytest.mark.parametrize("email, password, error", [(config.USER_EMAIL, config.USER_PASSWORD, 'Error: An account is already registered with your email address. Please log in.'),
                                                        ('a@b.c', 'xyzQ!!1234', 'Error: Please provide a valid email address.'),
                                                        ('temail@email.com', '', 'Error: Please enter an account password.')])
    def test_param_create_user_validation(self, email, password, error):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        account_page.register_user(email, password)
        error_msg = account_page.validation_msg()
        assert_that(error_msg).is_equal_to(error)
