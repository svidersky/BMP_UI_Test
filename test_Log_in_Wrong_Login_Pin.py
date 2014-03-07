#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''Тест проверяет невозможность авторизоваться с невалидными данными и вывод соответствующих ошибок''' 

from config import *
import time

driver.implicitly_wait(implicitly_wait)

# Проверка с несуществующим логином и пином

driver.get(base_url + "/press")
driver.find_element_by_link_text(u"Вход").click()
driver.find_element_by_id("login_login").send_keys("aqws")
driver.find_element_by_id("login_password").send_keys("1234")
driver.find_element_by_link_text(u"Войти").click()
for i in range(20):
    try:
        if u"Проверьте логин и PIN и попробуйте еще раз." == driver.find_element_by_id("login_login_error").text: break
    except: pass
    time.sleep(1)
else: pass

# Проверка с существующим логином и некорректным пином

driver.find_element_by_id("login_login").clear()      
driver.find_element_by_id("login_login").send_keys("0000")
driver.find_element_by_id("login_password").clear()
driver.find_element_by_id("login_password").send_keys("1234")
driver.find_element_by_link_text(u"Войти").click()
for i in range(20):
    try:
        if u"Не верный." == driver.find_element_by_id("login_password_error").text: break
    except: pass
    time.sleep(1)
else: pass
        
driver.quit()