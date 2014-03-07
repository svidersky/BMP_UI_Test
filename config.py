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

implicitly_wait = 7

# ---------------------

# driver's init

driver = webdriver.Firefox()
