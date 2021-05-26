import pytest
from assertpy import assert_that

import config
import allure
from datetime import datetime

import data
from pages.cart_page import CartPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("browser")
class TestGoToCart:

    @allure.title("Go to cart")
    @allure.description("Go to cart by click on 'Cart' tab")
    def test_go_to_cart_by_tab(self):
        cart_page = CartPage(self.driver)
        home_page = HomePage(self.driver)
        home_page.go_to_cart()
        empty_cart_msg = cart_page.empty_cart_msg()
        assert_that(empty_cart_msg).is_equal_to(data.MSG_EMPTY_CART)

    @allure.title("Go to cart")
    @allure.description("Go to cart by click on icon")
    def test_go_to_cart_by_icon(self):
        cart_page = CartPage(self.driver)
        home_page = HomePage(self.driver)
        home_page.go_to_cart_by_icon()
        empty_cart_msg = cart_page.empty_cart_msg()
        assert_that(empty_cart_msg).is_equal_to(data.MSG_EMPTY_CART)

    @allure.title("Go to cart")
    @allure.description("Go to cart by click view cart")
    def test_go_to_cart_by_add_product(self):
        cart_page = CartPage(self.driver)
        home_page = HomePage(self.driver)
        home_page.click_add_to_cart_button("Beanie")
        home_page.click_view_cart_button("Beanie")
        text_on_checkout_button = cart_page.text_on_checkout_button()
        assert_that(text_on_checkout_button).is_equal_to("Proceed to checkout")