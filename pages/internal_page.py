#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.page import Page


class InternalPage(Page):

    @property
    def header_button_signup(self):
        return self.driver.find_element_by_id("header_button_signup")

    @property
    def signupbox_link_login(self):
        return self.driver.find_element_by_id("signupbox_link_login")

    @property
    def login_field(self):
        return self.driver.find_element_by_id("login_login")

    @property
    def password_field(self):
        return self.driver.find_element_by_id("login_password")

    @property
    def login_button(self):
        return self.driver.find_element_by_id("button_login")

    @property
    def signup_button(self):
        return self.driver.find_element_by_id("button_signup")

    @property
    def link_user_login(self):
        return self.driver.find_element_by_id("link_user_login")

    @property
    def editaccount_button(self):
        return self.driver.find_element_by_id("button_editaccount")

    @property
    def exit_button(self):
        return self.driver.find_element_by_id("button_exit")

    @property
    def signup_login_field(self):
        return self.driver.find_element_by_id("signup_login")

    @property
    def signup_pin_field(self):
        return self.driver.find_element_by_id("signup_pin")

    @property
    def signup_email_field(self):
        return self.driver.find_element_by_id("signup_email")

    @property
    def user_subscribed_checkbox(self):
        return self.driver.find_element_by_name("user[subscribed]")

# errors ids

    @property
    def signup_login_error(self):
        return self.driver.find_element_by_id("signup_login_error")

    @property
    def signup_email_error(self):
        return self.driver.find_element_by_id("signup_email_error")

    @property
    def signup_pin_error(self):
        return self.driver.find_element_by_id("signup_pin_error")

    @property
    def login_pin_error(self):
        return self.driver.find_element_by_id("login_password_error")

    @property
    def login_login_error(self):
        return self.driver.find_element_by_id("login_login_error")

    @property
    def login_base_error(self):
        return self.driver.find_element_by_id("login_base_error")