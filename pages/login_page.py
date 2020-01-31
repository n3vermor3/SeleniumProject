from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def register_new_user(self ,email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_AREA).send_keys(email)
        time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REG_PASS_1).send_keys(password)
        time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True