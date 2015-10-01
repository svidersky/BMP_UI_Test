#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys
from pages.page import Page
from pages.internal_page import InternalPage
from pages.mobile_site import MobileSite
from pages.main_page import MainPage
from pages.list_page import ListPage
from pages.text_messages import TextMessages
from pages.actions_page import ActionsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.action_chains import ActionChains
import time


class ApplicationMobile(object):
    def __init__(self, driver, base_url):
        driver.get(base_url)
        self.wait = WebDriverWait(driver, 5)
        self.page = Page(driver, base_url)
        self.text_messages = TextMessages(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.mobile_site = MobileSite(driver, base_url)
        self.list_page = ListPage(driver, base_url)
        self.main_page = MainPage(driver, base_url)
        self.actions_page = ActionsPage(driver, base_url)
        self.action_chains = ActionChains(driver)


    def move_to_element(self, element):
        ac = self.action_chains
        ac.move_to_element(element)
        ac.perform()

    def switch_to_alert(self):
        ip = self.internal_page
        ip.driver.switch_to.alert.accept()

    def login(self, user):
        ms = self.mobile_site
        self.wait.until(presence_of_element_located((By.ID, "auth_link")))
        ms.auth_link.click()
        ms.auth_login_field.send_keys(Keys.COMMAND, "a")
        ms.auth_login_field.send_keys(Keys.DELETE)
        ms.auth_login_field.send_keys(user.username)
        ms.auth_pin_field.send_keys(Keys.COMMAND, "a")
        ms.auth_pin_field.send_keys(Keys.DELETE)
        ms.auth_pin_field.send_keys(user.password)
        ms.auth_button.click()

    def login_successful(self, user):
        assert self.wait.until(presence_of_element_located((By.XPATH, "//div[contains(@id,'footer_logout_link') and contains(text(),"+ user.username +")]")))

    def login_failed(self):
        if self.mobile_site.login_base_error.text != "":
            assert self.internal_page.login_base_error.text != ""

    def logout(self):
        ms = self.mobile_site
        ms.footer_logout_link.click()
        ms.profile_logout_button.click()
        self.wait.until(presence_of_element_located((By.ID, "auth_link")))