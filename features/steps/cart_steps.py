import os
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from browser_utils import wait_for_element, dismiss_popup_by_selector  # Updated import

feature_path = os.path.join(os.getcwd(), "features", "cart.feature")
scenarios(feature_path)

@given("I am logged in to SauceDemo")
def login_to_saucedemo(browser):
    browser.get("https://www.saucedemo.com/")
    wait_for_element(browser, "id", "login-button", timeout=10)
    dismiss_popup_by_selector(browser, ".popup-container")
    LoginPage(browser).login("standard_user", "secret_sauce")

@when("I add the first item to the cart")
def add_first_item_to_cart(browser):
    wait_for_element(browser, "class name", "inventory_item", timeout=10)
    InventoryPage(browser).add_first_item_to_cart()

@when("I go to the cart")
def go_to_cart(browser):
    wait_for_element(browser, "id", "shopping_cart_container", timeout=5)
    InventoryPage(browser).go_to_cart()

@then("I should see the item in my cart")
def verify_item_in_cart(browser):
    wait_for_element(browser, "class name", "cart_item", timeout=10)
    items = CartPage(browser).get_cart_items()
    assert len(items) > 0, "Cart should contain at least one item"
