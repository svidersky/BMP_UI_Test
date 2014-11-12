#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):

    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def user_0000(cls):
        return cls(username="0000", password="0000")

    @classmethod
    def random(cls):
        from random import randrange, randint
        return cls(username="test" + str(randint(0, 1000000)),
                   password= randrange(1000, 9999, 1),
                   email="test" + str(randint(0, 1000000)) + "@no-spam.ws")

    @classmethod
    def null(cls):
        return cls(username="", password="", email="")


    @classmethod
    def incorrect(cls):
        return cls(username=u"абвг",
                   password= u"абвг",
                   email=u"test" + "no-spam.ws")

    @classmethod
    def data_to_change(cls):
        return cls(password="1234", email="changed@email.com")

