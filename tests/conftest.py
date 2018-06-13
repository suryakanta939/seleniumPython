import pytest
import unittest
from baseUtils.invoke_browser import InvokeBrowser

@pytest.fixture()
def setUp():
    print("this will run before every test")
    yield
    print("this will run after everytest")

@pytest.fixture(scope="class")
def oneTimeSetUp(request,browser):
    driver=InvokeBrowser().opneBrowser(browser)
    print("this will run once before the test")
    if request.cls is not None:
        request.cls.driver=driver
    yield driver
    driver.quit()
    print("this will run once after the test")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType",help="here we will get the osType")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def ostype(request):
    return request.config.getoption("--osType")