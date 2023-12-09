import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope='function')
def browser_configs():
    browser.config.timeout = 2.0
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    browser.config.driver_options = options
    yield
    browser.quit()