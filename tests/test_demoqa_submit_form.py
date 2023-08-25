import os
from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data.users import User

picture_path = os.path.join(os.path.dirname(__file__), 'resources', 'test.png')


def test_successful_submit():
    # Arrange
    registration_page = RegistrationPage()

    student = User('Evgenii', 'Li', 'testacc@rambler.ru', 'Male', '7999888776',dict(month='March', day=22, year=1999),
                   'Maths', 'Music', picture_path, 'Odesskaya, bld. 24, appt. 23', 'NCR', 'Gurgaon')

    registration_page.open()

    # Act
    (
        registration_page
        .fill_first_name(student.first_name)
        .fill_last_name(student.last_name)
        .fill_user_email(student.email)
        .pick_gender(student.gender)
        .fill_user_phone_number(student.phone_number)
        .fill_date_of_birth(student.date_of_birth)

        .fill_subject(student.subject)
        .pick_hobby(student.hobby)

        .upload_picture(student.picture)

        .fill_current_address(student.current_address)
        .fill_state(student.state)
        .fill_city(student.city)

        .submit()
    )

    # Assert
    registration_page.should_have_registered(
        student.first_name,
        student.last_name,
        student.email,
        student.gender,
        student.phone_number,
        student.date_of_birth,
        student.subject,
        student.hobby,
        student.picture,
        student.current_address,
        student.state,
        student.city
    )
