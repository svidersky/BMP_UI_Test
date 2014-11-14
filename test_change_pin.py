from model.user import User
import time


def test_change_pin(app):
    app.login(User.user_0000())
    app.change_pin(User.user_0000_pin_1111())
    app.logout()
    app.login(User.user_0000())
    time.sleep(1)
    app.close_account_window()
    time.sleep(1)
    app.login(User.user_0000_pin_1111())
    app.login_successful(User.user_0000_pin_1111())

def test_change_pin_back(app):
    app.change_pin(User.user_0000())
    app.logout()