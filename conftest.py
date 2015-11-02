import pytest
from model.appplication_mobile import ApplicationMobile
from model.application_desktop import ApplicationDesktop
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser type")
    parser.addoption("--base_url", action="store", default="http://buymeapie.com/ru/press", help="base URL")
    parser.addoption("--client_type", action="store", default="desktop", help="client type")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture(scope="session")
def client_type(request):
    return request.config.getoption("--client_type")


@pytest.fixture(scope="session")
def app(request, browser_type, base_url, client_type):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
    elif browser_type == "ie":
        driver = webdriver.Ie()
    request.addfinalizer(driver.quit)
    if client_type == "desktop":
        return ApplicationDesktop(driver, base_url)
    elif client_type == "mobile":
        base_url = "http://m.buymeapie.com/"
        return ApplicationMobile(driver, base_url)