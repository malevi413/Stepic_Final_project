from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        """Проверяем, что находимся на странице регистрации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяем, что текущая ссылка это содержит login"""
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        """Проверяем, что форма авторизации есть"""
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_BTN), "Login link is not presented"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        self.browser.find_element(
            *LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REG_BTN).click()
