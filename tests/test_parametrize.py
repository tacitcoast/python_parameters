import pytest
from selene import browser, be, have
from selenium import webdriver


resolutions = [(1920, 1080), (1600, 1024), (1400, 1050), (3840, 2160), (3456, 2234), (320, 568), (375, 812), (390, 844), (412, 915)]
resolutions_descriptions = ['Full HD', 'WSXGA', 'SXGA+', '4K', 'Macbook Pro 16', 'iPhone 5s', 'iPhone X', 'iPhone 13 Pro', 'Sumsung Galaxy S20']


@pytest.fixture(params=resolutions, ids=resolutions_descriptions)
def browser_management(request):
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
    browser.config.window_width, browser.config.window_height = request.param

    yield

    browser.quit()


# Задание: переопределите параметр с помощью indirect параметризации на уровне теста
@pytest.mark.parametrize("browser_management", [(1920, 1080), (1600, 1024), (1400, 1050), (3840, 2160), (3456, 2234)],
                         ids=['Full HD', 'WSXGA', 'SXGA+', '4K', 'Macbook Pro 16'], indirect=True)
def test_github_desktop(browser_management):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    # assert browser.all("h5").element_by(have.exact_text("Sign in to GitHub"))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)


@pytest.mark.parametrize("browser_management", [(320, 568), (375, 812), (390, 844), (412, 915)],
                         ids=['iPhone 5s', 'iPhone X', 'iPhone 13 Pro', 'Sumsung Galaxy S20'], indirect=True)
def test_github_mobile(browser_management):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    # assert browser.all("h5").element_by(have.exact_text("Sign in to GitHub"))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)