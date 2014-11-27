from model.user import User
from model.product import Product


def test_add_product(app):
    app.login(User.user_0000())
    app.create_list()
    app.rename_list()
    app.add_product(Product.product_test())
    app.buy_product(Product.product_test())
    app.delete_list()
    app.logout()