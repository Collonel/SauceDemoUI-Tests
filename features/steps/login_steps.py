import os
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from browser_utils import wait_for_element, dismiss_popup_by_selector


feature_path = os.path.join(os.getcwd(), "features", "login.feature")
scenarios(feature_path)

@given("I am on the login page")
def go_to_login_page(browser):
    browser.get("https://www.saucedemo.com/")
    # 🛡️ Wait for login form to appear to avoid hangs
    wait_for_element(browser, "id", "login-button", timeout=10)
    # 🧼 Try to dismiss any popup (adjust selector as needed)
    dismiss_popup_by_selector(browser, ".popup-container")

@when("I login with valid credentials")
def login_with_valid_credentials(browser):
    LoginPage(browser).login("standard_user", "secret_sauce")

@when("I login with invalid credentials")
def login_with_invalid_credentials(browser):
    LoginPage(browser).login("invalid_user", "invalid_password")

@then("I should be redirected to the inventory page")
def verify_inventory_page(browser):
    assert "inventory.html" in browser.current_url

@then("I should see an error message")
def verify_error_message(browser):
    error = LoginPage(browser).get_error_message()
    assert "Epic sadface" in error
