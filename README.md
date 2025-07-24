This project automates UI testing for SauceDemo using Selenium WebDriver, Pytest-BDD, and the Page Object Model (POM). It includes both happy path and unhappy path scenarios for login and cart functionality.
📥 Setup Instructions
Prerequisites
- Python 3.11+ (Download)
- Chrome Browser (Latest version)
- PyCharm IDE (Recommended)
*Clone & Install Dependencies

Running the Tests
Command	Description
- pytest	Runs all tests in headless mode
- pytest --keep-open	Keeps browser open during tests
- pytest --headless	Forces headless mode (CI-friendly)
- pytest --html=report.html	Generates HTML test report

High Level Project Structure
saucedemo-tests/
├── features/
│   ├── login.feature       # BDD scenarios for login
│   ├── cart.feature        # BDD scenarios for cart
│   └── steps/             # Step definitions
├── pages/                 # Page Object Model
│   ├── base_page.py       # Core Selenium methods
│   ├── login_page.py      # Login page interactions
│   └── cart_page.py       # Cart page interactions
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Test configuration
└── requirements.txt       # Dependencies


Happy Testing! 🚀