import pytest
from selene import browser, be, have
from selenium import webdriver


# Настройки для запуска тестов, в связи с последними изменениями: в binary_location - прописываем путь до chrome, чтоб тесты шли в обычный хром
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = ('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

    yield

    browser.quit()


# Задание: сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
@pytest.fixture(params=[(1920, 1080), (1600, 1024), (1400, 1050), (3840, 2160), (3456, 2234)], ids=['Full HD', 'WSXGA', 'SXGA+', '4K', 'Macbook Pro 16'])
def setup_desktop_screen(request):
    browser.config.window_width, browser.config.window_height = request.param


@pytest.fixture(params=[(320, 568), (375, 812), (390, 844), (412, 915)], ids=['iPhone 5s', 'iPhone X', 'iPhone 13 Pro', 'Sumsung Galaxy S20'])
def setup_mobile_screen(request):
    browser.config.window_width, browser.config.window_height = request.param


def test_github_desktop(setup_desktop_screen):
    browser.open('https://github.com/')
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    # assert browser.all("h5").element_by(have.exact_text("Sign in to GitHub"))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)


def test_github_mobile(setup_mobile_screen):
    browser.open('https://github.com/')
    browser.element('[class=Button-content]').click()
    browser.element('[href="/login"]').click()
    assert browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
    # assert browser.all("h5").element_by(have.exact_text("Sign in to GitHub"))
    assert browser.element('#login_field').should(be.visible)
    assert browser.element('#password').should(be.visible)