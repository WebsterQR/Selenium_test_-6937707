class BasePage:
    def __init__(self, browser, url='', timeout=7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
