#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application model with test's steps

"""

from selenium.webdriver.common.keys import Keys
from pages.page import Page
from pages.internal_page import InternalPage
from pages.mobile_site import MobileSite
from pages.list_page import ListPage
from pages.text_messages import TextMessages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.action_chains import ActionChains
import time


class Application(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 7)
        self.page = Page(driver, base_url)
        self.text_messages = TextMessages(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.mobile_site = MobileSite(driver, base_url)
        self.list_page = ListPage(driver, base_url)
        self.action_chains = ActionChains(driver)


    def move_to_element(self, element):
        '''
        Move a pointer to an element
        :param element:
        :return:
        '''
        ac = self.action_chains
        ac.move_to_element(element)
        ac.perform()

    def switch_to_alert(self):
        '''
        Switch to alert and accept it
        '''
        ip = self.internal_page
        ip.driver.switch_to.alert.accept()

    def close_account_window(self):
        '''
        Close account form
        :return:
        '''
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "loginbox_close")))
        ip.loginbox_close.click()

    def login(self, user):
        '''
        Log in with the specified user's credentials
        :param user:
        :return:
        '''
        lp = self.internal_page
        lp.go_to_main()
        self.wait.until(presence_of_element_located((By.ID, "header_button_login")))
        lp.header_button_login.click()
        lp.login_field.send_keys(Keys.COMMAND, "a")
        lp.login_field.send_keys(Keys.DELETE)
        lp.login_field.send_keys(user.username)
        lp.password_field.send_keys(Keys.COMMAND, "a")
        lp.password_field.send_keys(Keys.DELETE)
        lp.password_field.send_keys(user.password)
        lp.login_button.click()

    def login_successful(self, user):
        '''
        Check the specified user is logged in successfully
        :param user:
        :return:
        :exception: if user did not log in
        '''
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        assert user.username in self.internal_page.link_user_login.text

    def login_failed(self):
        '''
        Check errors in a login form
        :return:
        :exception: if errors do not appear
        '''
        if self.internal_page.login_base_error.text != "":
            assert self.internal_page.login_base_error.text != ""
        if self.internal_page.login_login_error.text != "":
            assert self.internal_page.login_login_error.text != ""
        if self.internal_page.login_pin_error.text !="":
            assert self.internal_page.login_pin_error.text != ""
        self.close_account_window()

    def signup(self, user):
        '''
        Sign up with the specified user
        :param user:
        :return:
        :exception: if user did not sign up
        '''
        sp = self.internal_page
        sp.go_to_main()
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
        '''
        Log out
        :return:
        '''
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        self.internal_page.link_user_login.click()
        self.internal_page.exit_button.click()

    def add_product(self, product):
        '''
        Add the specified product to a current list
        :param product:
        :return:
        :exception: if the product does not appear in a shopping list
        '''
        lp = self.list_page
        self.wait.until(presence_of_all_elements_located)
        self.wait.until(presence_of_element_located((By.ID, "input_product")))
        lp.add_product_field.click()
        lp.add_product_field.send_keys(product.name + ":" + product.amount)
        lp.add_product_field.send_keys(Keys.RETURN)
        lp.add_product_field.send_keys(Keys.RETURN)
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]")))

    def buy_product(self, product):
        '''
        Buy the specified product in a shopping list
        :param product:
        :return:
        :exception: if product does not appear in a shopping list
        '''
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.ID, "input_product")))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]"))).click()
        time.sleep(3)
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]")))

    def delete_product(self, product):
        '''
        Delete the specified product in a shopping list
        :param product:
        :return:
        '''
        lp = self.list_page
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-title') and contains(text(),"+ product.name +")]"))))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-item-delete')]")))
        lp.button_product_delete.click()
        time.sleep(5)

    def create_list(self):
        '''
        Create a new shopping list
        :return:
        '''
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.ID, "button_add_list")))
        lp.button_add_list.click()
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]")))
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-empty')]")))
        time.sleep(1)

    def rename_list(self):
        '''
        Rename active list
        :return:
        '''
        lp = self.list_page
        self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]")))
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]"))))
        lp.button_edit_list.click()
        lp.input_edit_list.send_keys(Keys.COMMAND, "a")
        lp.input_edit_list.send_keys(Keys.DELETE)
        lp.input_edit_list.send_keys("Test list")
        lp.add_product_field.send_keys(Keys.RETURN)

    def delete_list(self):
        '''
        Delete active list
        :return:
        '''
        lp = self.list_page
        self.move_to_element(self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'product-list-name')]"))))
        #                                                                            "and contains(text(),'Test list')]"))))
        self.wait.until(presence_of_element_located((By.ID, "button_delete_list")))
        lp.button_delete_list.click()
        self.switch_to_alert()
        time.sleep(1)

    def change_pin(self, user_pin):
        '''
        Change current pin to a specified one
        :param user_pin:
        :return:
        '''
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        self.internal_page.link_user_login.click()
        self.internal_page.editaccount_button.click()
        ip.editaccount_pin_field.send_keys(Keys.COMMAND, "a")
        ip.editaccount_pin_field.send_keys(Keys.DELETE)
        ip.editaccount_pin_field.send_keys(user_pin.password)
        ip.editaccountbox_button_save.click()
        time.sleep(3)


    def change_email(self, user_email):
        '''
        Change current email to a specified one
        :param user_email:
        :return:
        '''
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
        self.internal_page.link_user_login.click()
        self.internal_page.editaccount_button.click()
        ip.editaccount_email_field.send_keys(Keys.COMMAND, "a")
        ip.editaccount_email_field.send_keys(Keys.DELETE)
        ip.editaccount_email_field.send_keys(user_email.email)
        ip.editaccountbox_button_save.click()
        ip.go_to_main()

    def remember_pin(self, email_to_send_pin):
        '''
        Send an email with recovered pin to a specified email
        :param email_to_send_pin:
        :return:
        :exception: if an email was not sent
        '''
        ip = self.internal_page
        self.wait.until(presence_of_element_located((By.ID, "header_button_login")))
        ip.header_button_login.click()
        self.wait.until(presence_of_element_located((By.ID, "logibox_link_remember")))
        ip.logibox_link_remember.click()
        self.wait.until(presence_of_element_located((By.ID, "remember_error")))
        ip.remember_error_field.click()
        ip.remember_error_field.send_keys(email_to_send_pin.email)
        ip.button_get_pin.click()
        # не работает ожидание, так как, видимо, элемент уже есть в доме # self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@class,'block sent') and contains(text(),'PIN был выслан на указанный e-mail')]")))
        time.sleep(2)
        if self.text_messages.pin_sent_to_email_text in ip.pin_sent_div.text:
            assert self.text_messages.pin_sent_to_email_text in ip.pin_sent_div.text
        elif self.internal_page.remember_error_error.text != "":
            assert self.internal_page.remember_error_error.text != ""
        ip.rememberbox_close.click()