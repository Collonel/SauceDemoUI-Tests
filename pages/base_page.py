from typing import Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

Locator = Tuple[By, str]

class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator: Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: Locator) -> None:
        self.find(locator).click()

    def send_keys(self, locator: Locator, text: str) -> None:
        self.find(locator).send_keys(text)

    def get_text(self, locator: Locator) -> str:
        return self.find(locator).text

    def is_displayed(self, locator: Locator) -> bool:
        try:
            return self.find(locator).is_displayed()
        except:
            return False