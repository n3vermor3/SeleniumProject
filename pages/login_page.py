from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def open_login(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()


    def register_new_user(self ,email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_AREA).send_keys(email)
        time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REG_PASS_1).send_keys(password)
        time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()


    def should_be_login_url(self):
        url = self.browser.current_url
        answ = url.find("login")
        assert answ != -1, "It isnt login page"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)