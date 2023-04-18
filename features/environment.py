from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context, test_name):
    """
    :param context: Behave context
    """

    service = Firefox_Service(executable_path=GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service)


    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver= context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
