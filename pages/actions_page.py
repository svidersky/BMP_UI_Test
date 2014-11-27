#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BMP_UI_Test2.pages.page import Page


class ActionsPage(Page):

    @property
    def email_field(self):
        return self.driver.find_element_by_name("email")

    @property
    def login_field(self):
        return self.driver.find_element_by_name("login")

    @property
    def operation_bar(self):
        return self.driver.find_element_by_id("operation")

    @property
    def new_login_field(self):
        return self.driver.find_element_by_name("new_login")

    @property
    def go_button(self):
        return self.driver.find_element_by_name("commit")