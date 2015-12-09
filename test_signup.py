"""
Sign up scenarios
"""

from model.user import User


def test_signup_with_valid_credentials(app):
    '''
    Test sign up with random user's credentials
    :param app:
    :return:
    '''
    app.signup(User.random())


def test_signup_with_blank_fields(app):
    '''
    Test sign up with no provided info
    :param app:
    :return:
    '''
    app.logout()
    app.signup(User.null())


def test_signup_with_incorrect_credentials(app):
    '''
    Test sign up with incorrect info
    :param app:
    :return:
    '''
    app.signup(User.incorrect())