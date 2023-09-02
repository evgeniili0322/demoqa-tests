import allure

from selene import browser, by, be


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    @allure.step('Open simple registration form')
    def open(self, element_group, element):
        if self.container.element(by.text(element)).should(be.clickable):
            self.container.element(by.text(element)).click()
        else:
            self.container.element(by.text(element_group)).click()
            self.container.element(by.text(element)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
