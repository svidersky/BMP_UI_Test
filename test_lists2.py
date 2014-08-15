from model.user import User


def test_add_product(app):
    app.login(User.user_0000())
    app.add_product()