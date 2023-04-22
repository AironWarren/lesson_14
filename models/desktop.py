from selene import browser


class Desktop:
    def __init__(self):
        self.button_login = browser.element('[href = "/login"]')

    def click_button_login(self):
        self.button_login.click()
