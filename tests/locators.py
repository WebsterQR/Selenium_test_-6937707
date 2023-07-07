from selenium.webdriver.common.by import By


class MainPageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button")


class LoginPageLocators:
    AUTH_LIST = (By.XPATH, '//*[@id="userSelect"]')
    LOGIN_BUtTON = (By.XPATH, '/html/body/div/div/div[2]/div/form/button')


class FunctionalPageLocators:
    DEPOSIT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]")
    AMOUNT_FIELD = (By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input")
    DEPOSIT_BUTTON_CONFIRM = (By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button")
    AMOUNT_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[3]")
    BALANCE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/strong[2]")
    TRANSACTIONS_BUTTON = (By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[1]")
    TRANSACTIONS_TABLE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/table/tbody")
    LABEL = (By.XPATH, '/html/body/div/div/div[2]/div/div[4]/div/form/div/label')
