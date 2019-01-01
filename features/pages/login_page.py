from selenium.webdriver.common.by import By
from framework.webapp import WebApp

from config import settings

class LoginPageLocator(object):
    # Home Page Locators

    USERNAME_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//input[@value='Login']")
    PROFILE_NAME = (By.CLASS_NAME, "user_name")
    ERROR_DIV = (By.CLASS_NAME, "alert-danger")


class LoginPage(WebApp):

    def fill(self, text, *locator):
        self.driver.instance.find_element(*locator).send_keys(text)

    def get_page_title(self):
        return self.driver.instance.title

    def verify_on_login_page(self):
        assert "Login" in self.driver.instance.title

    def login(self):
        self.fill(settings.correct_username, *LoginPageLocator.USERNAME_FIELD)
        self.fill(settings.correct_pwd, *LoginPageLocator.PASSWORD_FIELD)
        self.click_element(*LoginPageLocator.SUBMIT_BUTTON)

    def fill_correct_username(self):
        self.fill(settings.correct_username, *LoginPageLocator.USERNAME_FIELD)

    def fill_correct_pwd(self):
        self.fill(settings.correct_pwd, *LoginPageLocator.PASSWORD_FIELD)

    def fill_incorrect_username(self):
        self.fill(settings.incorrect_username, *LoginPageLocator.USERNAME_FIELD)

    def fill_random_pwd(self):
        self.fill(settings.random_pwd, *LoginPageLocator.PASSWORD_FIELD)

    def click_submit_btn(self):
        self.click_element(*LoginPageLocator.SUBMIT_BUTTON)

    def load_login_page(self):
        self.load_page(settings.login_page_url)

    def log_in(self):
        self.load_login_page()
        self.verify_on_login_page()
        self.fill_correct_username()
        self.fill_correct_pwd()
        self.click_submit_btn()
        self.verify_logged_in()
        return self.driver

    def verify_logged_in(self):
        element = self.wait_for_element(LoginPageLocator.PROFILE_NAME)
        assert settings.profile_name == element.text

    def verify_error_notification_is_displayed(self):
        element = self.wait_for_element(LoginPageLocator.ERROR_DIV)
        assert element.is_displayed()


