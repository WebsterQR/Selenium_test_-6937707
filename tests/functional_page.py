import datetime

from allure_commons._allure import step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_page import BasePage
from locators import FunctionalPageLocators


class FunctionalPage(BasePage):
    def get_fibonacci_num(self) -> int:
        day = FunctionalPage.get_current_day()
        result = FunctionalPage.fibonacci_func(day + 1)
        return result

    @step("Проверка начисления средств")
    def deposit(self, value: int):
        self.browser.find_element(*FunctionalPageLocators.DEPOSIT_BUTTON).click()
        self.browser.find_element(*FunctionalPageLocators.AMOUNT_FIELD).send_keys(str(value))
        self.browser.find_element(*FunctionalPageLocators.DEPOSIT_BUTTON_CONFIRM).click()

    @step("Сверка баланса")
    def shoud_be_correct_balance(self, value: int):
        balance_element = self.browser.find_element(*FunctionalPageLocators.BALANCE)
        assert balance_element.text == str(value)

    @step("Проверка списания средств")
    def withdrawl(self, value: int):
        self.browser.find_element(*FunctionalPageLocators.AMOUNT_BUTTON).click()
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(FunctionalPageLocators.LABEL, 'Amount to be Withdrawn :')

        )
        self.browser.find_element(*FunctionalPageLocators.AMOUNT_FIELD).send_keys(str(value))
        self.browser.find_element(*FunctionalPageLocators.AMOUNT_BUTTON).click()

    def transactions(self):
        self.browser.find_element(*FunctionalPageLocators.TRANSACTIONS_BUTTON)

    @staticmethod
    def fibonacci_func(n: int) -> int:
        if n == 1 or n == 2:
            return 1
        else:
            return FunctionalPage.fibonacci_func(n - 1) + FunctionalPage.fibonacci_func(n - 2)

    @staticmethod
    def get_current_day() -> int:
        return datetime.date.today().day
