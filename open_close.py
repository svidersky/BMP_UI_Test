from config import *
from selenium import webdriver
import unittest, time

class Setting_up(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(implicitly_wait)
        self.base_url = bmp_url
        self.verificationErrors = []
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()