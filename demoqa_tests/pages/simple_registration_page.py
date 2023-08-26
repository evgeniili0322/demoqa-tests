from selene import browser, be, have


class SimpleRegistrationPage:
    def open(self):
        browser.open('/text-box')

    def fill_full_name(self, full_name):
        browser.element('#userName').should(be.blank).type(full_name)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_permanent_address(self, value):
        browser.element('#permanentAddress').should(be.blank).type(value)
        return self

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, user):
        browser.element('#output #name').should(have.text(user.full_name))
        browser.element('#output #email').should(have.text(user.email))
        browser.element('#output #currentAddress').should(have.text(user.current_address))
        browser.element('#output #permanentAddress').should(have.text(user.permanent_address))
