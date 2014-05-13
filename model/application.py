#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.user import User
from selenium.webdriver.common.keys import Keys
from pages.page import Page
from pages.internal_page import InternalPage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.add_film_page import AddFilmPage
from pages.film_description_page import FilmDescriptionPage
from pages.main_page import MainPage
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
        self.login_page = LoginPage(driver, base_url)
        self.text_messages = TextMessages(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.user_management_page = UserManagementPage(driver, base_url)
        self.add_film_page = AddFilmPage(driver, base_url)
        self.film_description_page = FilmDescriptionPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)


    def login(self, user):
        lp = self.internal_page
        lp.header_button_signup.click()
        lp.signupbox_link_login.click()
        lp.login_field.send_keys(user.username)
        lp.password_field.send_keys(user.password)
        lp.login_button.click()
        try:
            self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
            assert user.username in self.internal_page.link_user_login.text

        except:
            assert self.text_messages.check_login_pin_text in self.internal_page.login_login_error.text

    def signup(self, user):
        sp = self.internal_page
        sp.header_button_signup.click()
        sp.signup_login_field.send_keys(user.username)
        time.sleep(1)
        sp.signup_pin_field.send_keys(Keys.COMMAND, "a")
        sp.signup_pin_field.send_keys(Keys.DELETE)
        sp.signup_pin_field.send_keys(user.password)
        time.sleep(1)
        sp.signup_email_field.send_keys(user.email)
        sp.user_subscribed_checkbox.click()
        sp.signup_button.click()
        try:
            self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
            assert user.username in self.internal_page.link_user_login.text

        except:
            pass

    def logout(self):
        self.internal_page.link_user_login.click()
        self.internal_page.exit_button.click()

    def ensure_logged_as(self, user):
        try:
            self.wait.until(presence_of_element_located((By.ID, "link_user_login")))
            assert user.username in self.internal_page.link_user_login.text

        except:
            assert self.text_messages.check_login_pin_text in self.internal_page.login_login_error.text

    def ensure_login_as(self, user):
        element = self.wait.until(visibility_of_element_located((By.CSS_SELECTOR, "nav, #loginform")))
        if element.tag_name == "nav":
            # we are on internal page
            if self.is_logged_in_as(user):
                return
            else:
                self.logout()
        self.login(user)

    def is_logged_in(self):
        return self.internal_page.is_this_page

    def is_logged_in_as(self, user):
        return self.is_logged_in() \
            and self.get_logged_user().username == user.username

    def is_not_logged_in(self):
        return self.login_page.is_this_page

    def get_logged_user(self):
        self.internal_page.user_profile_link.click()
        upp = self.user_profile_page
        upp.is_this_page
        return User(username=upp.user_form.username_field.get_attribute("value"),
                    email=upp.user_form.email_field.get_attribute("value"))


    def add_film(self, film):
        self.main_page.go_to_main()
        self.internal_page.add_film_button.click()
        self.add_film_page.film_title_field.send_keys(film.title)
        self.add_film_page.film_year_field.send_keys(film.year)
        self.add_film_page.add_film_submit.click()
        try:
            assert film.title in self.add_film_page.result_text
        except:
            assert self.add_film_page.field_required_text in self.add_film_page.field_is_required

    def search_film(self, film):
        self.page.go_to_main()
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.title")))
        self.main_page.film_search_field.send_keys(Keys.COMMAND, "a")
       # time.sleep(1)
        self.main_page.film_search_field.send_keys(Keys.DELETE)
        self.main_page.film_search_field.send_keys(film.title)
        self.main_page.film_search_field.send_keys(Keys.RETURN)
        #time.sleep(1)
        self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.title")))
        film_title_on_search_page = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "div.title")))
        assert film.title in film_title_on_search_page.text

    def remove_film(self, film):
        self.search_film(film)
        self.main_page.film_found.click()
        self.film_description_page.film_remove_button.click()
        self.wait.until(alert_is_present()).accept()