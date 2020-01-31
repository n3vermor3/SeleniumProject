from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "register_form")


class ProductPageLocators():
    ADD_TO_BUSKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    NAME_FROM_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRICE_FROM_MESSAGE = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#message")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")