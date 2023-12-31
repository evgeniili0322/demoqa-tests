import allure

from allure_commons.types import Severity

from demoqa_tests.application import app
from demoqa_tests.data.users import SimpleUser


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Evgenii Li')
@allure.feature('Simple registration from')
@allure.story('Assert registered user')
@allure.link('https://demoqa.com/text-box')
def test_successful_registration():
    # Arrange
    user = SimpleUser('Evgenii Li', 'testacc@rambler.ru', 'Odesskaya, bld. 24, appt. 23'
                      , 'G. Orekhovo-Zuevo Ul.uritskogo, bld. 66, appt. 24')

    app.open()

    app.left_panel.open_simple_registration_form()

    # Act
    (
        app.simple_registration_page
        .fill_full_name(user.full_name)
        .fill_user_email(user.email)
        .fill_current_address(user.current_address)
        .fill_permanent_address(user.permanent_address)
        .submit()
     )

    # Assert
    app.simple_registration_page.should_have_registered(user)
