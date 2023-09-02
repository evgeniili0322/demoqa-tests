from selene import browser

from demoqa_tests.components.panel import Panel
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.left_panel = Panel()
        self.registrations_page = RegistrationPage()
        self.simple_registration_page = SimpleRegistrationPage()

    def open(self):
        browser.open('/elements')


app = Application()
