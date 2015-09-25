#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BMP_UI_Test2.pages.page import Page


class TextMessages(Page):

    @property
    def login_check_pin_text(self):
        return u"Проверьте логин и PIN и попробуйте еще раз."

    @property
    def login_error_blank(self):
        return u"Поле Логин не должно быть пустым."

    @property
    def email_error_blank(self):
        return u"Поле email не должно быть пустым."

    @property
    def pin_error_blank(self):
        return u"PIN должен содержать 4 цифры."

    @property
    def login_base_error_blank_field(self):
        return u"Не заполнены обязательные поля."

    @property
    def signup_email_error_already_exist(self):
        return u"уже существует"

    @property
    def signup_login_error_already_exist(self):
        return u"уже существует"

    @property
    def signup_login_error_invalid_characters(self):
        return u"Можно использовать только буквы латинского алфавита (a–z), цифры и точки."

    @property
    def signup_email_error_invalid_characters(self):
        return u"Введенный email не является адресом электронной почты."

    @property
    def right_login_wrong_pin_error(self):
        return u"Не верный"

    @property
    def pin_sent_to_email_text(self):
        return u"PIN был выслан на указанный e-mail"