#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from selenium import webdriver
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(7)
        self.base_url = "http://buymeapie.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_all_fields_empty(self):
        driver = self.driver
        driver.get(self.base_url + "/contacts")
        driver.find_element_by_link_text("RU").click()
        driver.find_element_by_link_text("EN").click()
        driver.find_element_by_link_text("Log in").click()
        driver.find_element_by_css_selector("#login > a.button.blue").click()
        print "You did not provide any details for authentication."
        print driver.find_element_by_id("login_base_error")
        try: self.assertEqual("You did not provide any details for authentication.", driver.find_element_by_id("login_base_error").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
   
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
