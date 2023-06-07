import pytest
import faker

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestGuestAddToBasketFromProductPage():
    """Класс для тестирования работы незарегистрированного пользователя"""

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """Тест, гость может добавить товар в корзину"""
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    # @pytest.mark.parametrize('link1', [0, 1, 2, 3, 4, 5, 6,
    #                                    pytest.param(7, marks=pytest.mark.xfail),
    #                                    8, 9])
    # def test_guest_can_add_product_to_basket(browser, link1):
    #     link1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link1}"
    #     page = ProductPage(browser, link1)
    #     page.open()
    #     page.add_product_to_basket()
    #     page.solve_quiz_and_get_code()
    #     page.should_be_message_about_adding()
    #     page.should_be_message_basket_total()
    @pytest.mark.need_review
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        """Тест, что гостю не показывается сообщение об успешном добавлении товара"""
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """Тест, что гость не видит товара в корзине открытой со страницы товара"""
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_is_empty()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_product_button()
        page.should_be_disappeared_success_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """Тест, что у гостя есть возможность перейти на страницу авторизации со страницы товара"""
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    """Класс для тестирования работы зарегистрированного пользователя.
    Перед тестом происходит регистрация условного пользователя на сайте.
    """

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Подготовка данных для теста"""
        # Открываем страницу регистрации
        login_page = LoginPage(
            browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()
        # Генерируем почту, прописываем пароль и регистрируем нового пользователя
        f = faker.Faker()
        email = f.email()
        password = "Martin654321"
        # Регистрируем нового пользователя
        login_page.register_new_user(email, password)
        # Проверяем, что пользователь авторизован
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Проверка возможности добавить товар в корзину пользователем"""
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()

    @pytest.mark.skip
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
