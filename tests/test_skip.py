"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser

from models.desktop import Desktop
from models.mobile import Mobile

desktop = Desktop()
mobile = Mobile()


def test_github_desktop(browser_parametrize):
    size = browser.driver.get_window_size()
    if size['width'] < 1800:
        pytest.skip()

    desktop.click_button_login()


def test_github_mobile(browser_parametrize):
    size = browser.driver.get_window_size()
    if size['width'] > 550:
        pytest.skip()

    mobile.click_drop_down_list()
    mobile.click_button_login()
