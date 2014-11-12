from model.user import User


def test_signup_with_valid_credentials(app):
    app.signup(User.random())

def test_signup_with_blank_fields(app):
    app.logout()
    app.signup(User.null())

def test_signup_with_incorrect_credentials(app):
    app.signup(User.incorrect())