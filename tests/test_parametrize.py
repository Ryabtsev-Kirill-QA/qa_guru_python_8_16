"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1366, 768), (360, 800), (390, 844)])
def browser_size(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


desktop_only = pytest.mark.parametrize("browser_size", [(1920, 1080), (1366, 768)], indirect=True)
mobile_only = pytest.mark.parametrize("browser_size", [(360, 800), (390, 844)], indirect=True)


@desktop_only
def test_github_desktop(browser_size):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))


@mobile_only
def test_github_mobile(browser_size):
    browser.open("https://github.com/")
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))
