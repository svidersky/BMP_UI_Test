from model.user import User


def test_login_with_valid_credentials(app):
    app.login(User.user_0000())
    app.login_successful(User.user_0000())


#def test_login_with_invalid_credentials(app):
 #   app.logout()
  #  app.login(User.random())


#def test_login_with_blank_fields(app):
 #   app.login(User.null())