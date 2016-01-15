"""
Sign up scenarios
"""
from model.user import User
from model.additional_functions import skip_if_not_run_all


@skip_if_not_run_all
def test_signup_with_valid_credentials(app):
    '''
    Test sign up with random user's credentials
    :param app:
    :return:
    '''
    app.signup(User.random())
    app.logout()


def test_signup_with_blank_fields(app):
    '''
    Test sign up with no provided info
    :param app:
    :return:
    '''
    app.signup(User.null())


def test_signup_with_incorrect_credentials(app):
    '''
    Test sign up with incorrect info
    :param app:
    :return:
    '''
    app.signup(User.incorrect())