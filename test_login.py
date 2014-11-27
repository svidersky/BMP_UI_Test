from model.user import User

def test_login_with_valid_credentials(app):
    app.login(User.user_0000())
    app.login_successful(User.user_0000())

def test_login_with_blank_fields(app):
    app.logout()
    app.login(User.null())
    app.login_failed()

def test_login_with_invalid_credentials(app):
    app.login(User.random())
    app.login_failed()

