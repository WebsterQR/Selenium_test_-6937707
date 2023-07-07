from allure_commons._allure import step

from locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException
from base_page import BasePage


class MainPage(BasePage):
    @step("Проверка открытия страницы")
    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.CUSTOMER_LOGIN_BUTTON)
        login_link.click()

    def should_be_login_link(self,):
        assert self.is_element_present(*MainPageLocators.CUSTOMER_LOGIN_BUTTON)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
