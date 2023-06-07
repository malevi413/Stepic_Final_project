from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_ENTER_REG = (By.NAME, "registration_submit")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BTN = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")

class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner p")