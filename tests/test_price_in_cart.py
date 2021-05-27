import allure
import pytest
from assertpy import assert_that

from pages.home_page import HomePage


@pytest.mark.usefixtures("browser")
class TestPriceInCart:

    @allure.title("Check price in cart near the cart icon")
    @allure.description("Check if price in the cart is correct for 1 product")
    def test_go_to_cart_by_tab(self):
        home_page = HomePage(self.driver)
        list_of_products = ['Beanie', 'Cap']
        home_page.add_multiple_product(list_of_products)
        value_of_products = home_page.sum_of_added_product_to_cart(list_of_products)
        value_in_cart = home_page.check_price_near_cart_icon()
        assert_that(value_in_cart).is_equal_to(value_of_products)

