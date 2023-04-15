from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


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
        self.driver.find_element(*self.FUND_TRANSFER_BUTTON).click()

    def correct_required_fields(self):
        self.driver.find_element(*self.PAYERS_ACCOUNT_FIELD).send_keys('121219')
        self.driver.find_element(*self.PAYEES_ACCOUNT_FIELD).send_keys('121221')
        self.driver.find_element(*self.AMOUNT_FIELD).send_keys('500')
        self.driver.find_element(*self.DESCRIPTION_FIELD).send_keys('cash')
        sleep(2)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def incorrect_required_fields(self):
        self.driver.find_element(*self.PAYERS_ACCOUNT_FIELD).send_keys('555555')
        self.driver.find_element(*self.PAYEES_ACCOUNT_FIELD).send_keys('121221')
        self.driver.find_element(*self.AMOUNT_FIELD).send_keys('500')
        self.driver.find_element(*self.DESCRIPTION_FIELD).send_keys('cash')
        sleep(2)

    def verify_fund_transfer(self):
        text = self.driver.find_element(*self.FUND_TRANSFER_DETAILS).text
        assert text == "Fund Transfer Details"

    def fund_transfer_page(self):
        self.driver.refresh()
        sleep(5)
        refreshed_page_text = self.driver.find_element(*self.REFRESH_FUND_TRANSFER_DETAILS).text
        assert refreshed_page_text == "Fund transfer"
        self.driver.quit()
        # THIS IS NOT WORKING

    def verify_account_doesnt_exist(self, pop_up):
        alert = self.driver.wait.until(EC.alert_is_present())
        text = alert.text
        print(f"This is the alert: {text}")
        assert text == pop_up
        self.driver.quit()





