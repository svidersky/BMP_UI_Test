#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from selenium import webdriver
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);
        self.driver.implicitly_wait(10)
        self.base_url = "http://buymeapie.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_Log_in_successful(self):
        driver = self.driver
        driver.get(self.base_url + "/press")
        driver.find_element_by_link_text("RU").click()
        driver.find_element_by_link_text("EN").click()
        driver.find_element_by_link_text(u"Log in").click()
        driver.find_element_by_id("login_login").clear()
        driver.find_element_by_id("login_login").send_keys("sv40")
        driver.find_element_by_id("login_password").clear()
        driver.find_element_by_id("login_password").send_keys("1111")
        driver.find_element_by_css_selector("#login > a.button.blue").click()
        try: self.assertEqual("sv40", driver.find_element_by_link_text("sv40").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='ng-app']/div[2]/div/div/div/div").click()
        try: self.assertEqual(u"Список покупок", driver.find_element_by_xpath("//div[@id='ng-app']/div[2]/div/div/div/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
