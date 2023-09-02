import os
import allure

from allure_commons.types import Severity

from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User, Gender
from datetime import datetime


picture_path = os.path.join(os.path.dirname(__file__), 'resources', 'test.png')


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Registration form')
@allure.story('Assert registered user')
@allure.link('https://demoqa.com/automation-practice-form')
def test_successful_registration():
    # Arrange
    registration_page = RegistrationPage()

    student = User('Evgenii', 'Li', 'testacc@rambler.ru', Gender.male.value, '7999888776', datetime(1999, 3, 22),
                   'Maths', 'Music', picture_path, 'Odesskaya, bld. 24, appt. 23', 'NCR', 'Gurgaon')

    registration_page.open()

    # Act
    registration_page.register_user(student)

    # Assert
    registration_page.should_have_registered(student)
