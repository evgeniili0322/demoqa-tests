import pytest

from selenium import webdriver
from selene import browser

from demoqa_tests.utils import attach


options = webdriver.ChromeOptions()


@pytest.fixture(scope='function', autouse=True)
def browser_opt(request):
    browser_version = "100.0"
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    options.add_argument('window-size=2560,1440')

    browser.config.driver = webdriver.Remote(
        'https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
