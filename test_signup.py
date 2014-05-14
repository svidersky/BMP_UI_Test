from model.user import User


def test_signup_with_valid_credentials(app):
    app.signup(User.random())


def test_signup_with_invalid_credentials(app):
    app.logout()
    app.signup(User.null())
