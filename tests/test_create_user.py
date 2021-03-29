from datetime import datetime

import pytest
import config

from pages.home_page import HomePage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("browser")
class TestCreateUser:

    def test_create_user(self):
        home_page = HomePage(self.driver)
        account_page = MyAccountPage(self.driver)
        generate_email = f"email{datetime.now().microsecond}@test.com"
        generate_password = f"password{datetime.now().microsecond}"
        home_page.go_to_my_account_page()
        account_page.register_user(generate_email, generate_password)
        account_page.is_logout_link_displayed()
