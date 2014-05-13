#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.page import Page


class TextMessages(Page):

    @property
    def check_login_pin_text(self):
        return u"Проверьте логин и PIN и попробуйте еще раз."