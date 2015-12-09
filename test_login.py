"""
Log in scenarios
"""

from model.user import User


def test_login_with_valid_credentials(app):
    '''
    Test log in with existing user. Make sure that log in successful
    :param app:
    :return:
    '''
    app.login(User.user_0000())
    app.login_successful(User.user_0000())


def test_login_with_blank_fields(app):
    '''
    Test log in with no provided info. Make sure that log in failed
    :param app:
    :return:
    '''
    app.logout()
    app.login(User.null())
    app.login_failed()


def test_login_with_invalid_credentials(app):
    '''
    Test log in with random credentials. Make sure that log in failed
    :param app:
    :return:
    '''
    app.close_account_window()
    app.login(User.random())
    app.login_failed()