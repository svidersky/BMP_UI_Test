from model.user import User

def test_show_user_info(app):
    app.login(User.user_actions())
    app.show_user_info(User.user_svidersky())