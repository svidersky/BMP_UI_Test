#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from selenium import webdriver
import unittest, time

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(7)
        self.base_url = "http://buymeapie.com/"
        self.verificationErrors = []
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/press")
        driver.find_element_by_link_text(u"Вход").click()
        driver.find_element_by_id("login_login").send_keys("aqws")
        driver.find_element_by_id("login_password").send_keys("1234")
        driver.find_element_by_link_text(u"Войти").click()
        for i in range(20):
            try:
                if u"Проверьте логин и PIN и попробуйте еще раз." == driver.find_element_by_id("login_login_error").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
     
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
