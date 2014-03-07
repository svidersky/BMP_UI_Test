#!/usr/bin/env python 
# -*- coding: utf-8 -*-

'''Тест проверяет невозможность авторизоваться с невалидными данными и вывод соответствующих ошибок''' 

from config import *
import time
driver = Init()
driver = driver.driver_init()
#driver.implicity_wait(impl_wait)

testing = Auth()
testing = testing.authorizing()

        
driver.quit()