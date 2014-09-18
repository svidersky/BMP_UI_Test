# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://phpd.buymeapie.com"

    def test_ads(self):
        driver = self.driver

# 4 free
        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_RU&os_version=7.0&app_id=757682453&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_US&os_version=7.0&app_id=757682453&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_DE&os_version=7.0&app_id=757682453&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)
    
# 3 pro

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_RU&os_version=7.0&app_id=491322606&os_name=ios")
        self.assertEqual("{\"enabled\":false}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_US&os_version=7.0&app_id=491322606&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"bank_of_america\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_DE&os_version=7.0&app_id=491322606&os_name=ios")
        self.assertEqual("{\"enabled\":false}", driver.find_element_by_css_selector("pre").text)

# android


        driver.get(self.base_url + "/ad?install_date=1388534400&app_version=3.4.11&long=&region=en_RU&os_version=8.0&app_id=com.buymeapie.bmap&os_name=Android+Google&lat=")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?install_date=1388534400&app_version=3.4.11&long=&region=en_US&os_version=8.0&app_id=com.buymeapie.bmap&os_name=Android+Google&lat=")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)


# 3 free

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_RU&os_version=7.0&app_id=491297400&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_US&os_version=7.0&app_id=491297400&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"bank_of_america\"}", driver.find_element_by_css_selector("pre").text)

        driver.get(self.base_url + "/ad?app_version=3.4.9&region=en_DE&os_version=7.0&app_id=491297400&os_name=ios")
        self.assertEqual("{\"enabled\":true,\"type\":\"admob\"}", driver.find_element_by_css_selector("pre").text)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
