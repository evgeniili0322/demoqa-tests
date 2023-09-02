import allure

from selene import browser, be, have


class SimpleRegistrationPage:
    def open(self):
        browser.open('/text-box')

    @allure.step('Fill user name')
    def fill_full_name(self, full_name):
        browser.element('#userName').should(be.blank).type(full_name)
        return self

    @allure.step('Fill user email')
    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    @allure.step('Fill user current address')
    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    @allure.step('Fill user permanent address')
    def fill_permanent_address(self, value):
        browser.element('#permanentAddress').should(be.blank).type(value)
        return self

    @allure.step('Submit')
    def submit(self):
        browser.element('#submit').click()

    @allure.step('Assert registered user')
    def should_have_registered(self, user):
        browser.element('#output #name').should(have.text(user.full_name))
        browser.element('#output #email').should(have.text(user.email))
        browser.element('#output #currentAddress').should(have.text(user.current_address))
        browser.element('#output #permanentAddress').should(have.text(user.permanent_address))
