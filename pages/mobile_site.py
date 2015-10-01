#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pages.page import Page


class MobileSite(Page):

    @property
    def auth_link(self):
        return self.driver.find_element_by_id("auth_link")

    @property
    def signup_link(self):
        return self.driver.find_element_by_id("signup_link")

    @property
    def auth_login_field(self):
        return self.driver.find_element_by_id("auth_login")

    @property
    def auth_pin_field(self):
        return self.driver.find_element_by_id("auth_pin")

    @property
    def auth_button(self):
        return self.driver.find_element_by_id("auth_button")

    @property
    def remember_pin_link(self):
        return self.driver.find_element_by_id("remember_pin_link")

    @property
    def signup_pin_field(self):
        return self.driver.find_element_by_id("signup_pin")

    @property
    def signup_email_field(self):
        return self.driver.find_element_by_id("signup_email")

    @property
    def signup_subscribe_checkbox(self):
        return self.driver.find_element_by_id("signup_subscribe")

    @property
    def signup_button(self):
        return self.driver.find_element_by_id("signup_button")

    @property
    def create_list_button(self):
        return self.driver.find_element_by_id("create_list_button")

    @property
    def footer_logout_link(self):
        return self.driver.find_element_by_id("footer_logout_link")

    @property
    def profile_logout_button(self):
        return self.driver.find_element_by_id("profile_logout_button")

    @property
    def list_manager_button(self):
        return self.driver.find_element_by_id("list_manager_button")

    @property
    def edit_list_title(self):
        return self.driver.find_element_by_id("edit_list_title")

    @property
    def add_product_button(self):
        return self.driver.find_element_by_id("add_product_button")

    @property
    def revert_all_bought_button(self):
        return self.driver.find_element_by_id("revert_all_bought_button")

    @property
    def remove_all_bought_button(self):
        return self.driver.find_element_by_id("remove_all_bought_button")

    @property
    def input_products(self):
        return self.driver.find_element_by_id("input_products")

    @property
    def remove_products_button(self):
        return self.driver.find_element_by_id("remove_products_button")

    @property
    def login_base_error(self):
        return self.driver.find_element_by_id("login_base_error")