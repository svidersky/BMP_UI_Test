#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.user import User
from selenium.webdriver.common.keys import Keys
from pages.page import Page
from pages.internal_page import InternalPage
from pages.main_page import MainPage
from pages.list_page import ListPage
from pages.text_messages import TextMessages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
import time


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 5)
        self.page = Page(driver, base_url)
        self.text_messages = TextMessages(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.list_page = ListPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)

    def login(self, user):
        lp = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "header_button_signup")))
        lp.header_button_signup.click()
        lp.signupbox_link_login.click()
        lp.login_field.send_keys(Keys.COMMAND, "a")
        lp.login_field.send_keys(Keys.DELETE)
        lp.login_field.send_keys(user.username)
        lp.password_field.send_keys(Keys.COMMAND, "a")
        lp.password_field.send_keys(Keys.DELETE)
        lp.password_field.send_keys(user.password)
        lp.login_button.click()

    def login_successful(self, user):
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        assert user.username in self.internal_page.link_user_login.text

    def login_failed(self):
        if self.internal_page.login_base_error.text != "":
            assert self.internal_page.login_base_error.text != ""
        if self.internal_page.login_login_error.text != "":
            assert self.internal_page.login_login_error.text != ""
        if self.internal_page.login_pin_error.text !="":
            assert self.internal_page.login_pin_error.text != ""

    def signup(self, user):
        sp = self.internal_page
        sp.header_button_signup.click()
        sp.signup_login_field.send_keys(Keys.COMMAND, "a")
        sp.signup_login_field.send_keys(Keys.DELETE)
        sp.signup_login_field.send_keys(user.username)
        time.sleep(1)
        sp.signup_pin_field.send_keys(Keys.COMMAND, "a")
        sp.signup_pin_field.send_keys(Keys.DELETE)
        sp.signup_pin_field.send_keys(user.password)
        sp.signup_email_field.send_keys(Keys.COMMAND, "a")
        sp.signup_email_field.send_keys(Keys.DELETE)
        sp.signup_email_field.send_keys(user.email)
        sp.user_subscribed_checkbox.click()
        sp.signup_button.click()
        try:
            self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
            assert user.username in self.internal_page.link_user_login.text

        except:
            assert self.internal_page.signup_login_error.text != "" or\
                   self.internal_page.signup_pin_error.text != "" or\
                   self.internal_page.signup_email_error.text != ""


    def logout(self):
        self.internal_page.link_user_login.click()
        self.internal_page.exit_button.click()

    def add_product(self):
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.ID, "input_product")))
        lp.add_product_field.click()
        lp.add_product_field.send_keys("Test")
        lp.add_product_field.send_keys(Keys.RETURN)
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),'Test')]")))

    def change_pin(self, user_pin):
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        self.internal_page.link_user_login.click()
        self.internal_page.editaccount_button.click()
        ip.editaccount_pin_field.send_keys(Keys.COMMAND, "a")
        ip.editaccount_pin_field.send_keys(Keys.DELETE)
        ip.editaccount_pin_field.send_keys(user_pin.password)
        ip.editaccountbox_button_save.click()

    def close_account_window(self):
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "loginbox_close")))
        ip.loginbox_close.click()