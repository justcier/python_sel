import pytest
import config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateUser:

    def test_create_user(self):
        home_page = HomePage(self.driver)
        new_account = MyAccountPage(self.driver)
        home_page.go_to_my_account_page()
        new_account.register_user(config.USER_EMAIL, config.USER_PASSWORD)

