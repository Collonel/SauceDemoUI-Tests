from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, 'button.btn_inventory')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def add_first_item_to_cart(self) -> str:
        item_name = self.get_text(self.ITEM_NAMES)
        self.click(self.ADD_TO_CART_BUTTONS)
        return item_name

    def go_to_cart(self) -> None:
        self.click(self.CART_LINK)