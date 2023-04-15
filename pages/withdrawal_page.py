from selenium.webdriver.common.by import By
from pages.base_page import Page


class Withdrawal(Page):
    WITHDRAWAL_BUTTON = (By.CSS_SELECTOR, 'a[href="WithdrawalInput.php"]')
    ACCOUNT_NO_FIELD = (By.CSS_SELECTOR, 'input[name="accountno"]')
    AMOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="ammount"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="desc"]')
    WITHDRAWAL_SUCCESS = (By.CSS_SELECTOR, 'p.heading3')

    def withdrawal_button(self):
        self.driver.find_element(*self.WITHDRAWAL_BUTTON).click()
        # THIS IS FAILING

    def account_number(self, account_number_input):
        self.driver.find_element(*self.ACCOUNT_NO_FIELD).send_keys(account_number_input)

    def amount_number(self, amount):
        self.driver.find_element(*self.AMOUNT_FIELD).send_keys(amount)

    def withdrawal_desc(self, input):
        self.driver.find_element(*self.DESCRIPTION_FIELD).send_keys(input)

    def verify_withdrawal(self):
        text = self.driver.find_element(*self.WITHDRAWAL_SUCCESS).text
        assert text == "Transaction details of Withdrawal for Account 121219"

