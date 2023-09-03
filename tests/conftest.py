import os
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selene import browser

from demoqa_tests.utils import attach


options = webdriver.ChromeOptions()


def pytest_addoption(parser):
    parser.addoption(
        '--browser_url'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_opt(request):
    options.add_argument('window-size=2560,1440')
    browser.config.base_url = 'https://demoqa.com'

    browser_url = request.config.getoption('--browser_url')

    if browser_url is not None:
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": '100.0',
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)

        browser.config.driver = webdriver.Remote(
            command_executor=f'{browser_url}',
            options=options
        )
    else:
        browser.config.driver_options = options

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
