from model.user import User
from model.product import Product


def test_create_list(app):
    app.login(User.user_0000())
    app.create_list()

def test_rename_list(app):
    app.rename_list()

def test_add_product(app):
    app.add_product(Product.product_test())

def test_buy_product(app):
    app.buy_product(Product.product_test())

def test_delete_list(app):
    app.delete_list()

def logout(app):
    app.logout()