# browser_utils.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import pytest

def wait_for_element(browser, by, value, timeout=10):
    """Wait for a specific element to be present on the page."""
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        try:
            browser.quit()  # Ensure browser closes cleanly
        except Exception as e:
            print(f"[ERROR] Failed to quit browser: {e}")
        pytest.fail(f"[FAILURE] Element '{value}' not found within {timeout}s — browser force-closed due to possible freeze.")


def dismiss_popup_by_selector(browser, selector):
    """Try to find and remove a popup by CSS selector."""
    try:
        popup = browser.find_element(By.CSS_SELECTOR, selector)
        browser.execute_script("arguments[0].remove();", popup)
    except:
        pass  # No popup found — continue silently
