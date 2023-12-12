"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1366, 768)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(360, 800), (390, 844)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


def test_github_desktop(desktop_browser):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))


def test_github_mobile(mobile_browser):
    browser.open("https://github.com/")
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))
