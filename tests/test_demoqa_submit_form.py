import os
from selene import browser, be, have, by
from selenium.webdriver import Keys
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.Users import Student

picture_path = os.path.join(os.path.dirname(__file__), 'resources', 'test.png')
student = Student('Evgenii', 'Li', 'testacc@rambler.ru', 'Male', 7999888776, dict(month='March', day=22, year=1999),
                  'Maths', 'Music', picture_path)


def test_successful_submit():
    registration_page = RegistrationPage()
    registration_page.open()

    # Act
    registration_page.fill_first_name(student.first_name)
    registration_page.fill_last_name(student.last_name)
    registration_page.fill_user_email(student.email)
    registration_page.pick_gender(student.gender)
    registration_page.fill_user_phone_number(student.phone_number)

    registration_page.fill_date_of_birth(student.date_of_birth)

    registration_page.fill_subject(student.subject)

    registration_page.pick_hobby(student.hobby)

    registration_page.upload_picture(student.picture)

    browser.element('#currentAddress').should(be.blank).type('Odesskaya, bld. 24, appt. 23')

    browser.element('#react-select-3-input').type('u').press_enter()
    browser.element('#react-select-4-input').type('').send_keys(Keys.ARROW_DOWN).press_enter()

    browser.element('#submit').click()

    # Assert
    browser.element('table').all('td').even.should(have.exact_texts(
        'Evgenii Li',
        'testacc@rambler.ru',
        'Male',
        '7999888776',
        '22 March,1999',
        'Maths',
        'Music',
        'test.png',
        'Odesskaya, bld. 24, appt. 23',
        'Uttar Pradesh Agra'
    ))
