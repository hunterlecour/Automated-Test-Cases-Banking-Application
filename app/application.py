from pages.fund_transfer_page import Fund_Transfer
from pages.login_page import Login
from pages.password_page import Password
from pages.withdrawal_page import Withdrawal

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.fund_transfer_page = Fund_Transfer(self.driver)
        self.login_page = Login(self.driver)
        self.password_page = Password(self.driver)
        self.withdrawal_page = Withdrawal(self.driver)


