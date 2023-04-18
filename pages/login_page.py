import allure
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from allure_commons.types import AttachmentType


class Login(Page):
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[name="uid"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_CLICK = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOGOUT_CLICK = (By.CSS_SELECTOR, 'a[href="Logout.php"]')
    ACTUAL_RESULT = (By.CSS_SELECTOR, 'marquee.heading3')

    def open_bank_app(self):
        self.open_url('https://www.demo.guru99.com/V4/')

    def login(self, login_input):
        self.input_text(login_input, *self.LOGIN_INPUT)

    def login_id_wrong(self, invalid_login_input):
        self.input_text(invalid_login_input, *self.LOGIN_INPUT)

    def password(self, password_input):
        self.input_text(password_input, *self.PASSWORD_INPUT)

    def password_wrong(self, invalid_password_input):
        self.input_text(invalid_password_input, *self.PASSWORD_INPUT)

    def login_click(self):
        self.click(*self.LOGIN_CLICK)


    def logout_click(self):
        self.click(*self.LOGOUT_CLICK)

    def verify_login(self):
        expected_result = "Welcome To Manager's Page of Guru99 Bank"
        actual_result = self.driver.find_element(*self.ACTUAL_RESULT).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='login-test-1.png', attachment_type=AttachmentType.PNG)

    def verify_login_error(self):

        # Wait for the alert to appear
        alert = self.driver.wait.until(EC.alert_is_present())
        #  Check if the alert exists
        if alert:
            print("Log in error alert exists")
        else:
            print("Log in error alert does not exist")
        alert.accept()
        sleep(1)
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='login-test-2.png', attachment_type=AttachmentType.PNG)
        self.driver.quit()

    def verify_logout(self):
        alert = self.driver.wait.until(EC.alert_is_present())
        actual_text = alert.text
        expected_text = 'You Have Succesfully Logged Out!!'
        assert expected_text == actual_text, f"Expected alert text not found, but found {actual_text}"
        alert.dismiss()
        # Taking Screenshot
        allure.attach(self.driver.get_screenshot_as_png(), name='login-test-3.png', attachment_type=AttachmentType.PNG)
        self.driver.quit()

