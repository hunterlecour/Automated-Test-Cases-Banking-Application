from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
import allure
from allure_commons.types import AttachmentType

class Fund_Transfer(Page):
    FUND_TRANSFER_BUTTON = (By.CSS_SELECTOR, "ul.menusubnav [href= 'FundTransInput.php']")
    PAYERS_ACCOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="payersaccount"]')
    PAYEES_ACCOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="payeeaccount"]')
    AMOUNT_FIELD = (By.CSS_SELECTOR, 'input[name="ammount"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'input[name="desc"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    FUND_TRANSFER_DETAILS = (By.CSS_SELECTOR, 'p[align="center"]')
    REFRESH_FUND_TRANSFER_DETAILS = (By.CSS_SELECTOR, 'td[align="center"] p.heading3')

    def click_fund_transfer(self):
        self.click(*self.FUND_TRANSFER_BUTTON)

    def correct_required_fields(self):
        self.input_text('138547', *self.PAYERS_ACCOUNT_FIELD)
        self.input_text('138548', *self.PAYEES_ACCOUNT_FIELD)
        self.input_text('500', *self.AMOUNT_FIELD)
        self.input_text('cash', *self.DESCRIPTION_FIELD)

    def click_submit(self):
        self.click(*self.SUBMIT_BUTTON)

    def incorrect_required_fields(self):
        self.input_text('555555', *self.PAYERS_ACCOUNT_FIELD)
        self.input_text('138547', *self.PAYEES_ACCOUNT_FIELD)
        self.input_text('500', *self.AMOUNT_FIELD)
        self.input_text('cash', *self.DESCRIPTION_FIELD)

    def verify_fund_transfer(self):
        text = self.driver.find_element(*self.FUND_TRANSFER_DETAILS).text
        assert text == "Fund Transfer Details"
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='fund-transfer-1.png', attachment_type=AttachmentType.PNG)


    def verify_transfer_page(self):
        self.driver.refresh()
        alert = self.driver.wait.until(EC.alert_is_present())
        alert.accept()
        refreshed_page_text = self.driver.find_element(*self.REFRESH_FUND_TRANSFER_DETAILS).text
        assert refreshed_page_text == "Fund transfer"
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='fund-transfer-2.png',
                      attachment_type=AttachmentType.PNG)
        self.driver.quit()


    def verify_account_doesnt_exist(self, pop_up):
        alert = self.driver.wait.until(EC.alert_is_present())
        text = alert.text
        print(f"This is the alert: {text}")
        assert text == pop_up
        self.driver.quit()






