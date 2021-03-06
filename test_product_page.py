from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        email = str(time.time()) + "@example.com"
        password = "qwerty67890"
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser,link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()


    link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()   
        page.should_not_be_success_message()


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_busket_button()
        page.add_to_busket()
        page.solve_quiz_and_get_code()
        page.check_name_of_product()
        page.check_price_of_product()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", 
                     marks=pytest.mark.xfail(reason="Несоответсвие наименований")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket_button()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    page.check_name_of_product()
    page.check_price_of_product()


link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket_button()
    page.add_to_busket()
    page.should_not_be_success_message()
    
   
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()   
    page.should_not_be_success_message()


@pytest.mark.xfail 
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_busket_button()
    page.add_to_busket()
    page.should_dissapear_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.check_basket()     