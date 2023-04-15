from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class Login(Page):
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[name="uid"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_CLICK = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOGOUT_CLICK = (By.CSS_SELECTOR, 'a[href="Logout.php"]')
    ACTUAL_RESULT = (By.CSS_SELECTOR, 'marquee.heading3')

    def open_bank_app(self):
        self.open_url('https://www.demo.guru99.com/V4/')

    def login(self, login_input):
        loginx = self.driver.find_element(*self.LOGIN_INPUT)
        loginx.clear()
        loginx.send_keys(login_input)

    def login_id_wrong(self, invalid_login_input):
        in_loginx = self.driver.find_element(*self.LOGIN_INPUT)
        in_loginx.clear()
        in_loginx.send_keys(invalid_login_input)

    def password(self, password_input):
        passwordx = self.driver.find_element(*self.PASSWORD_INPUT)
        passwordx.clear()
        passwordx.send_keys(password_input)

    def password_wrong(self, invalid_password_input):
        in_passwordx = self.driver.find_element(*self.PASSWORD_INPUT)
        in_passwordx.clear()
        in_passwordx.send_keys(invalid_password_input)

    def login_click(self):
        self.driver.find_element(*self.LOGIN_CLICK).click()

    def logout_click(self):
        self.driver.find_element(*self.LOGOUT_CLICK).click()
        # NOT WORKING

    def verify_login(self):
        expected_result = "Welcome To Manager's Page of Guru99 Bank"
        actual_result = self.driver.find_element(*self.ACTUAL_RESULT).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
        sleep(1)
        # Taking Screenshot
        self.driver.get_screenshot_as_file('images/ss1.png')

    def verify_login_error(self):
        # Wait for the alert to appear
        alert = self.driver.wait.until(EC.alert_is_present())
        #  Check if the alert exists
        if alert:
            print("Alert exists")
        else:
            print("Alert does not exist")

        self.driver.quit()

    def verify_logout(self):
        alert = self.driver.wait.until(EC.alert_is_present())
        text = alert.text
        print(f"This is the alert: {text}")
        assert text == 'You Have Successfully Logged Out!!'

