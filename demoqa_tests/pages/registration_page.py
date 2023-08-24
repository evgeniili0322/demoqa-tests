import os

from selene import browser, be, by, command
from collections import namedtuple

Date = namedtuple("Date", "month day year")


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def pick_gender(self, value):
        browser.element(f'[value={value}] +label').click()

    def fill_user_phone_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, value):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element(by.text(value['month'])).click()
        browser.element('.react-datepicker__year-select').click()
        (browser.element('.react-datepicker__year-select').element(f'[value="{value["year"]}"]')
            .perform(command.js.scroll_into_view).click())
        browser.element(f'.react-datepicker__day--0{value["day"]}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    def pick_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(value)
