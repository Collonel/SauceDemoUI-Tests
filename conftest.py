import pytest
import os
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")
    parser.addoption("--keep-open", action="store_true", help="Keep browser open after all tests")
    parser.addoption("--report-dir", default="reports", help="Directory to store test reports")


@pytest.fixture(scope="session")  # Changed to session scope
def browser(request):
    # Setup
    temp_profile = tempfile.mkdtemp()
    options = Options()

    # Browser configuration
    options.add_argument("--start-maximized")
    options.add_argument(f"--user-data-dir={temp_profile}")
    options.add_argument("--disable-features=AutofillServerCommunication")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    else:
        options.add_experimental_option("detach", False)

    # WebDriver initialization with your fallback logic
    try:
        driver_path = ChromeDriverManager().install()
        print(f"Using ChromeDriver from: {driver_path}")
    except Exception:
        driver_path = "D:\\4GCapital\\drivers\\chromedriver.exe"
        print(f"Falling back to local ChromeDriver: {driver_path}")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    # Yield the browser to all tests
    yield driver

    # Teardown - only after all tests complete
    if not request.config.getoption("--keep-open"):
        try:
            driver.quit()
        except Exception as e:
            print(f"Warning during cleanup: {str(e)}")
            try:
                driver.service.process.kill()
            except:
                pass


@pytest.fixture(autouse=True)
def cleanup_between_tests(browser):
    # Clear cookies between tests while keeping browser open
    browser.delete_all_cookies()
    browser.execute_script("window.localStorage.clear();")
    browser.execute_script("window.sessionStorage.clear();")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    # Take screenshot on failure
    if rep.when == "call" and rep.failed:
        report_dir = item.config.getoption("--report-dir")
        os.makedirs(report_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        browser = item.funcargs.get('browser')
        if browser:
            browser.save_screenshot(f"{report_dir}/failure_{item.name}_{timestamp}.png")


def pytest_configure(config):
    # Ensure report directory exists
    report_dir = config.getoption("--report-dir")
    os.makedirs(report_dir, exist_ok=True)

    # Add HTML report if plugin available
    if config.pluginmanager.hasplugin("html"):
        config.option.htmlpath = os.path.join(report_dir, "report.html")