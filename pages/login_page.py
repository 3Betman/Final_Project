from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        assert "login" in self.browser.current_url, "'login' is not in url"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self, email, password):
        email = str(time.time()) + "@fakemail.org"
        password = "qwertzuio"

        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        assert input_email.is_displayed(), "Input field for email is not visible!"
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        assert input_password.is_displayed(), "Input field for password is not visible!"
        input_password.send_keys(password)

        check_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CHECK)
        assert check_password.is_displayed(), "Input field for check password is not visible!"
        check_password.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        assert button.is_displayed(), "IRegistration button is not visible!"
        button.click()





