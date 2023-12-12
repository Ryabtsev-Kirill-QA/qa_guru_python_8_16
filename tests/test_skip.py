"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.fixture(params=[(1920, 1080), (1366, 768), (360, 800), (390, 844)])
def browser_size(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param[0] >= 1012:
        return "desktop_browser"
    else:
        return "mobile_browser"


def test_github_desktop(browser_size):
    if browser_size != "desktop_browser":
        pytest.skip(reason="Not for desktop version")
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))


def test_github_mobile(browser_size):
    if browser_size != "mobile_browser":
        pytest.skip(reason="Not for mobile version")
    browser.open("https://github.com/")
    browser.element('.js-details-target.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing('login'))
