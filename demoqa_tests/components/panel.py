from selene import browser, by


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, element_group, element):
        self.container.element(by.text(element_group)).click()
        self.container.element(by.text(element)).click()

    def open_simple_registration_form(self):
        self.open('Elements', 'Text Box')
