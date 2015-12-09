"""
Change email scenarios
"""

from model.user import User
import time


def test_change_pin(app):
    '''
    Login with existing user. Change pin to a new one. Log in with old credentials. Log in with new credentials.
    :param app:
    :return:
    '''
    app.login(User.user_0000())
    app.change_pin(User.user_0000_pin_1111())
    app.logout()
    app.login(User.user_0000())
    app.close_account_window()
    time.sleep(1)
    app.login(User.user_0000_pin_1111())
    app.login_successful(User.user_0000_pin_1111())


def test_change_pin_back(app):
    '''
    Change pin back to old credentials. Remember this old pin.
    :param app:
    :return:
    '''
    app.change_pin(User.user_0000())
    app.logout()
    app.remember_pin(User.user_0000())