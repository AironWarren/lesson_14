"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from models.desktop import Desktop
from models.mobile import Mobile

desktop = Desktop()
mobile = Mobile()


def test_github_desktop(open_browser_desktop):
    desktop.click_button_login()


def test_github_mobile(open_browser_mobile):
    mobile.click_drop_down_list()
    mobile.click_button_login()
