"""
Conftest.py is a setup and config file for the whole project

"""

import pytest
from model.application import Application

from selenium import webdriver


def pytest_addoption(parser):
    '''
    Function parses --browser and --base_url values from predefined ones or from a command line
    '''
    parser.addoption("--browser", action="store", default="firefox", help="browser type")
    parser.addoption("--base_url", action="store", default="http://buymeapie.com/ru/press", help="base URL")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="session")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)