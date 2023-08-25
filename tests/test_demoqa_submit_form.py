import os
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import Student

picture_path = os.path.join(os.path.dirname(__file__), 'resources', 'test.png')
student = Student('Evgenii', 'Li', 'testacc@rambler.ru', 'Male', '7999888776', dict(month='March', day=22, year=1999),
                  'Maths', 'Music', picture_path, 'Odesskaya, bld. 24, appt. 23', 'NCR', 'Gurgaon')


def test_successful_submit():
    registration_page = RegistrationPage()

    registration_page.open()

    # Act
    registration_page.register_user(student)

    # Assert
    registration_page.should_have_registered(student)
