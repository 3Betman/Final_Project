from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket has items, but should be empty"

    def should_be_correct_text_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        basket_text = "Your basket is empty"
        assert basket_text in text, "Basket empty-text does not match"

