#!/usr/bin/env python 
# -*- coding: utf-8 -*-

''' ''' 

#  init 
from config import *
import time
driver = Init()
driver = driver.driver_init()
driver.implicitly_wait(impl_wait)

# 
      
# quit 
driver.quit()