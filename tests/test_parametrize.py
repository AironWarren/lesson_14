"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest

from models.desktop import Desktop
from models.mobile import Mobile

desktop_parametrize = pytest.mark.parametrize("browser_parametrize", ["Desktop"], indirect=True)
mobile_parametrize = pytest.mark.parametrize("browser_parametrize", ["Mobile"], indirect=True)

desktop = Desktop()
mobile = Mobile()


@desktop_parametrize
def test_github_desktop(browser_parametrize):
    desktop.click_button_login()


@mobile_parametrize
def test_github_mobile(browser_parametrize):
    mobile.click_drop_down_list()
    mobile.click_button_login()
