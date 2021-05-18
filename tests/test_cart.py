import pytest
from assertpy import assert_that

import config
import allure
from datetime import datetime

import data
from pages.cart_page import CartPage


@pytest.mark.usefixtures("browser")
class TestCart:

    @allure.title("Go to cart")
    @allure.description("Go to cart by click on 'Cart' tab")
    def test_go_to_cart_by_tab(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        empty_cart_msg = cart_page.empty_cart_validation_msg()
        assert_that(empty_cart_msg).is_equal_to(data.MSG_EMPTY_CART)

    @allure.title("Go to cart")
    @allure.description("Go to cart by click on icon")
    def test_go_to_cart_by_icon(self):
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart_by_icon()
        empty_cart_msg = cart_page.empty_cart_validation_msg()
        assert_that(empty_cart_msg).is_equal_to(data.MSG_EMPTY_CART)

