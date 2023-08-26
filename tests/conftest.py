import pytest
from selenium import webdriver
from selene import browser

options = webdriver.ChromeOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt():
    options.add_argument('--headless')
    options.add_argument('window-size=1920,1080')
    browser.config.driver_options = options
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
    