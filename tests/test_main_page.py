from main_page import MainPage
from login_page import LoginPage
from functional_page import FunctionalPage


def test_scenario(browser):
    link = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    page = MainPage(browser, link)
    login_page = LoginPage(browser)
    functional_page = FunctionalPage(browser)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page.auth(login='Harry Potter')
    N = functional_page.get_fibonacci_num()
    functional_page.deposit(N)
    functional_page.shoud_be_correct_balance(N)
    functional_page.withdrawl(N)
    functional_page.shoud_be_correct_balance(0)
