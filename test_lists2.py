"""
Test shopping list features
"""

from model.user import User
from model.product import Product


def test_prepare(app):
    '''
    Log in with existing user and delete active list
    :param app:
    :return:
    '''
    app.login(User.user_0000())
    app.delete_list()


def test_create_list(app):
    '''
    Create a new list
    :param app:
    :return:
    '''
    app.create_list()


def test_rename_list(app):
    '''
    Rename active list
    :param app:
    :return:
    '''
    app.rename_list()


def test_add_product(app):
    '''
    Add the specified item to a current shopping list
    :param app:
    :return:
    '''
    app.add_product(Product.product_test())


def test_buy_product(app):
    '''
    Buy the specified item from a current shopping list
    :param app:
    :return:
    '''
    app.buy_product(Product.product_test())


#def test_delete_product(app):
 #   app.delete_product(Product.product_test())


def test_delete_list(app):
    '''
    Delete active shopping list
    :param app:
    :return:
    '''
    app.delete_list()


def test_logout(app):
    '''
    Log out
    :param app:
    :return:
    '''
    app.logout()