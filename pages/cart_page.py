from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, 'inventory_item_name')
    REMOVE_BUTTONS = (By.CSS_SELECTOR, 'button.cart_button')

    def get_cart_items(self) -> list[str]:
        return [item.text for item in self.driver.find_elements(*self.CART_ITEMS)]

    def remove_first_item(self) -> None:
        self.click(self.REMOVE_BUTTONS)