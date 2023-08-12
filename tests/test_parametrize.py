"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(params=resolutions, ids=resolutions_descriptions)
def browser_management(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    browser.config.window_width, browser.config.window_height = request.param

    yield

    browser.quit()


@pytest.fixture()
def browser():
    pass


def test_github_desktop(browser):
    pass


def test_github_mobile(browser):
    pass