from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET_FORM)
        assert add_to_basket.is_displayed(), "Add_to_Basket Button is not visible!"
        add_to_basket.click()

    def solve_task(self):
        assert self.solve_quiz_and_get_code()
        assert True

    def should_be_correct_text(self):
        text = self.browser.find_element(*ProductPageLocators.TEXT_ADDED_TO_BASKET).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == text, "Basket was not updated"

    def should_be_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.COST_OF_BASKET).text
        assert price == basket_price, "Price is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_ADDED_TO_BASKET), "Success message is presented, but should not be"

    def should_not_appear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.TEXT_ADDED_TO_BASKET), "Success message did not disappear"


