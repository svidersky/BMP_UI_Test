#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from selenium import selenium
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*firefox", "http://buymeapie.com/")
        self.selenium.start()
    
    def test_untitled(self):
        sel = self.selenium
        sel.open("/contacts")
        sel.click("link=EN")
        sel.click("link=RU")
        sel.wait_for_page_to_load("5000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
