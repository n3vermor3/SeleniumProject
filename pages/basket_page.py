from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def check_basket(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_NULL), \
            "Basket isnt null"