import pytest
from selenium import webdriver


#TODO Относительный путь до Chromedriver
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome("/Users/evgeniy/Documents/Workspace/SimbirSoft_test/Selenium_test_-6937707/chromedriver")
    yield browser
    print("\nquit browser..")
    browser.quit()