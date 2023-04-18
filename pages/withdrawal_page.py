from selenium.webdriver.common.by import By
from pages.base_page import Page
import allure
from allure_commons.types import AttachmentType


class Withdrawal(Page):
    WITHDRAWAL_BUTTON = (By.CSS_SELECTOR, 'a[href="WithdrawalInput.php"]')
    ACCOUNT_NO_FIELD = (By.CSS_SELECTOR, 'input[name="accountno"]')
    AMOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="ammount"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="desc"]')
    WITHDRAWAL_SUCCESS = (By.CSS_SELECTOR, 'p.heading3')

    def withdrawal_button(self):
        self.click(*self.WITHDRAWAL_BUTTON)

    def account_number(self, account_number_input):
        self.input_text(account_number_input, *self.ACCOUNT_NO_FIELD)

    def amount_number(self, amount):
        self.input_text(amount, *self.AMOUNT_FIELD)

    def withdrawal_desc(self, input):
        self.input_text(input, *self.DESCRIPTION_FIELD)

    def verify_withdrawal(self):
        text = self.driver.find_element(*self.WITHDRAWAL_SUCCESS).text
        assert text == "Transaction details of Withdrawal for Account 121219"
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='withdrawal-test-1.png',
                      attachment_type=AttachmentType.PNG)

