from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_add_to_busket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BUSKET), "Button 'add to busket' is not presented"
    
    
    def add_to_busket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET)
        button.click()


    def check_name_of_product(self):
        text = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        mesg = self.browser.find_element(*ProductPageLocators.NAME_FROM_MESSAGE).text
        assert text == mesg, "'Имена не совпадают'"

        
    def check_price_of_product(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_FROM_MESSAGE).text
        assert price1 == price2, "'Цены не совпадают'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    
    def should_dissapear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
