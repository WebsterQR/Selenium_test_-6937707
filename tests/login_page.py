from allure_commons._allure import step

from base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.support.ui import Select


class LoginPage(BasePage):
    @step("Проверка авторизации под конкретным пользователем")
    def auth(self, login: str):
        self._get_user(login)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUtTON).click()

    def _get_user(self, user: str):
        choise = self.browser.find_element(*LoginPageLocators.AUTH_LIST)
        se = Select(choise)
        se.select_by_visible_text(user)
