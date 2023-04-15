from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Password(Page):
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[href="PasswordInput.php"]')
    OLD_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="oldpassword"]')
    NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="newpassword"]')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="confirmpassword"]')

    def click_change_customer(self):
        self.driver.find_element(*self.CHANGE_PASSWORD_BUTTON).click()

    def incorrect_old_password(self, incorrect_input):
        self.driver.find_element(*self.OLD_PASSWORD_FIELD).send_keys(incorrect_input)

    def new_password_credential(self, new_password_input):
        self.driver.find_element(*self.NEW_PASSWORD_FIELD).send_keys(new_password_input)
        self.driver.find_element(*self.CONFIRM_PASSWORD_FIELD).send_keys(new_password_input)

    def verify_password_error(self):
        alert = self.driver.wait.until(EC.alert_is_present())
        text = alert.text
        print(f"This is the alert: {text}")
        assert text == "Old Password is incorrect"
        self.driver.quit()

