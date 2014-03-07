#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''Тест проверяет авторизацию пользователя с валидными данными''' 

#  init 
from config import *
import time
driver = Init()
driver = driver.driver_init()
driver.implicitly_wait(impl_wait)

# Попытка авторизации с валидными данными

driver.get(base_url + "/press")
driver.find_element_by_link_text(u"Вход").click()
driver.find_element_by_id("login_login").clear()
driver.find_element_by_id("login_login").send_keys(user_good_login)
driver.find_element_by_id("login_password").clear()
driver.find_element_by_id("login_password").send_keys(user_good_pass)
driver.find_element_by_css_selector("#login > a.button.blue").click()
driver.find_element_by_link_text(user_good_login).text
              
# quit 

driver.quit()