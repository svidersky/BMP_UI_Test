from model.user import User

def test_login_with_valid_credentials(app):
    app.login_m(User.user_0000())
    app.login_successful_m(User.user_0000())