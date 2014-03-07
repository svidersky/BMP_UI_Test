#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from selenium import webdriver

# production
base_url = "http://buymeapie.com/" 

# phpd4
#base_url = "http://alpha4.buymeapie.corp/" 

# phpd-test
#base_url = "http://test.buymeapie.com/"

# ---------------------

# user_credentials

user_good_login = '0000'
user_good_pass = '0000'

user_bad_login = 'kkk'
user_bad_pass = '1234'

# ---------------------

# implicitly_wait

impl_wait = 7

# ---------------------

# self.driver's init

class Init(object):
    def __init__(self):
        pass
        
    def driver_init(self):    
        current_driver = webdriver.Firefox()
        return current_driver
    
class Auth(object):
    driver = webdriver.Firefox()
    def __init__(self):
        pass
    def authorizing(self):
        self.driver.get(base_url + "/press")
        self.driver.find_element_by_link_text(u"Вход").click()
        self.driver.find_element_by_id("login_login").clear()
        self.driver.find_element_by_id("login_login").send_keys(user_good_login)
        self.driver.find_element_by_id("login_password").clear()
        self.driver.find_element_by_id("login_password").send_keys(user_good_pass)
        self.driver.find_element_by_css_selector("#login > a.button.blue").click()