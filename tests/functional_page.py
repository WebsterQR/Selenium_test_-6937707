import datetime
import time

from base_page import BasePage
from locators import FunctionalPageLocators
class FunctionalPage(BasePage):
    def get_fibonacci_num(self) -> int:
        day = FunctionalPage.get_current_day()
        result = FunctionalPage.fibonacci_func(day + 1)
        return result
    def deposit(self, value: int):
        self.browser.find_element(*FunctionalPageLocators.DEPOSIT_BUTTON).click()
        self.browser.find_element(*FunctionalPageLocators.DEPOSIT_AMOUNT).send_keys(str(value))
        self.browser.find_element(*FunctionalPageLocators.DEPOSIT_BUTTON_CONFIRM).click()

    def shoud_be_correct_balance(self, value: int):
        balance_element = self.browser.find_element(*FunctionalPageLocators.BALANCE)
        assert balance_element.text == str(value)

    def withdrawl(self, value: int):
        #TODO Зарефакторить эту функцию и deposit. Объединить в одну с использованием параметра
        self.browser.find_element(*FunctionalPageLocators.WITHDRAWL_BUTTON).click()
        #TODO Избавиться от хардкода time.sleep() и заменить на ожидание элемента
        time.sleep(3)
        self.browser.find_element(*FunctionalPageLocators.WITHDRAWL_AMOUNT).send_keys(str(value))
        self.browser.find_element(*FunctionalPageLocators.WITHDRAWL_CONFIRM).click()

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