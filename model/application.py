#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from BMP_UI_Test2.pages.page import Page
from BMP_UI_Test2.pages.internal_page import InternalPage
from BMP_UI_Test2.pages.main_page import MainPage
from BMP_UI_Test2.pages.list_page import ListPage
from BMP_UI_Test2.pages.text_messages import TextMessages
from BMP_UI_Test2.pages.actions_page import ActionsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.action_chains import ActionChains
import time


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 15)
        self.page = Page(driver, base_url)
        self.text_messages = TextMessages(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.list_page = ListPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.actions_page = ActionsPage(driver, base_url)
        self.action_chains = ActionChains(driver)


    def move_to_element(self, element):
        ac = self.action_chains
        ac.move_to_element(element)
        ac.perform()

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

    def add_product(self, product):
        lp = self.list_page
        self.wait.until(presence_of_all_elements_located)
        self.wait.until(presence_of_element_located((By.ID, "input_product")))
        lp.add_product_field.click()
        lp.add_product_field.send_keys(product.name + ":" + product.amount)
        lp.add_product_field.send_keys(Keys.RETURN)
        lp.add_product_field.send_keys(Keys.RETURN)
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]")))

    def buy_product(self, product):
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.ID, "input_product")))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]"))).click()
        time.sleep(3)
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]")))

    def delete_product(self, product):
        lp = self.list_page
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]"))))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-delete')]")))
        lp.button_product_delete.click()
        time.sleep(5)

    def create_list(self):
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.ID, "button_add_list")))
        lp.button_add_list.click()
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]")))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-empty')]")))
        time.sleep(1)

    def rename_list(self):
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]")))
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]"))))
        lp.button_edit_list.click()
        lp.input_edit_list.send_keys(Keys.COMMAND, "a")
        lp.input_edit_list.send_keys(Keys.DELETE)
        lp.input_edit_list.send_keys("Test list")
        lp.add_product_field.send_keys(Keys.RETURN)

    def delete_list(self):
        lp = self.list_page
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name') and contains(text(),'Test list')]"))))
        self.wait.until(presence_of_element_located((By.ID, "button_delete_list")))
        lp.button_delete_list.click()

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

    def change_email(self, user_email):
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        self.internal_page.link_user_login.click()
        self.internal_page.editaccount_button.click()
        ip.editaccount_email_field.send_keys(Keys.COMMAND, "a")
        ip.editaccount_email_field.send_keys(Keys.DELETE)
        ip.editaccount_email_field.send_keys(user_email.email)
        ip.editaccountbox_button_save.click()

    def remember_pin(self, email_to_send_pin):
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "header_button_signup")))
        ip.header_button_signup.click()
        ip.signupbox_link_login.click()
        self.wait.until(presence_of_element_located((By.ID, "logibox_link_remember")))
        ip.logibox_link_remember.click()
        self.wait.until(presence_of_element_located((By.ID, "remember_error")))
        ip.remember_error_field.click()
        ip.remember_error_field.send_keys(email_to_send_pin.email)
        ip.button_get_pin.click()

    def show_user_info(self, user_info):
        time.sleep(2)
        ip = self.internal_page
        ip.go_to_main()
        time.sleep(2)
        ap = self.actions_page
        self.wait.until(presence_of_element_located((By.ID, "login")))
        ap.login_field.click()
        ap.login_field.send_keys(user_info.username)
        ap.go_button.click()
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(text(),'login: svid')]")))

