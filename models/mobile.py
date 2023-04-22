from selene import browser


class Mobile:
    def __init__(self):
        self.drop_down_list = browser.element('.flex-1 .Button-label')
        self.button_login = browser.element('[href = "/login"]')

    def click_drop_down_list(self):
        self.drop_down_list.click()

    def click_button_login(self):
        self.button_login()
