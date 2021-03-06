#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Product(object):
    '''
    Products to interact with in a shopping list
    '''

    def __init__(self, name="", amount="", color=""):
        self.name = name
        self.amount = amount
        self.color = color

    @classmethod
    def product_test(cls):
        return cls(name="Test", amount="5", color="")