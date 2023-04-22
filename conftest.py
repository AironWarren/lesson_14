import pytest
from selene import browser


@pytest.fixture(scope="session")
def open_browser_desktop():
    browser.config.window_height = 1800
    browser.config.window_width = 1800
    browser.open('https://github.com/')

    yield

    browser.quit()


@pytest.fixture(scope="session")
def open_browser_mobile():
    browser.config.window_height = 1200
    browser.config.window_width = 550
    browser.open('https://github.com/')

    yield

    browser.quit()


@pytest.fixture(params=["Desktop", "Mobile"])
def browser_parametrize(request):
    if request.param == "Desktop":
        browser.config.window_height = 1800
        browser.config.window_width = 1800
    if request.param == "Mobile":
        browser.config.window_height = 1200
        browser.config.window_width = 550

    browser.open('https://github.com/')

    yield

    browser.quit()
