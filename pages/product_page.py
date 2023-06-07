from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_add_product_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Add button is not presented"

    def should_be_message_about_adding(self):
        # Проверяем, что название товара присутствует в сообщении о добавлении
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name_basket == product_name_page, \
            f"Product names in page and basket are not the same! {product_name_page} != {product_name_basket}"
        # print(product_name_page)
        # print(product_name_basket)

    def should_be_message_basket_total(self):
        # Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices in page and basket are not the same! {product_price} != {basket_price}"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        """Ожидаем, что сообщение о добавлении не появится"""

        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is not dissapeared, but should be"

    def go_to_basket_page(self):
        """Переход в корзину
        """

        basket_link = self.browser.find_element(
            *ProductPageLocators.BASKET_LINK)
        basket_link.click()
