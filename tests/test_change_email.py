"""
Change email scenarios
"""

from model.user import User


def test_change_email(app):
    '''
    Change pin, remember new pin
    :param app:
    :return:
    '''
    app.login(User.user_0000())
    app.change_email(User.user_0000_pin_1111())
    app.logout()
    app.remember_pin(User.user_0000_pin_1111())


def test_change_email_back(app):
    '''
    Change pin back, remember old pin
    :param app:
    :return:
    '''
    app.login(User.user_0000())
    app.change_email(User.user_0000())
    app.logout()
    app.remember_pin(User.user_0000())