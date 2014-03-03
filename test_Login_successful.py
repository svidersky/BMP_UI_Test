#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(implicitly_wait)
        self.base_url = bmp_url
        self.verificationErrors = []

    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/press")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_id("login_login").clear()
        driver.find_element_by_id("login_login").send_keys("0000")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("0000")
        driver.find_element_by_css_selector("#login > a.button.blue").click()
        try: self.assertEqual("0000", driver.find_element_by_link_text("0000").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
