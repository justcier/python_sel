import logging

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import config


@pytest.fixture()
def browser(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(config.SITE)
    request.cls.driver = driver
    yield
    driver.quit()
