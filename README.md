This project automates UI testing for SauceDemo using Selenium WebDriver, Pytest-BDD, and the Page Object Model (POM). It includes both happy path and unhappy path scenarios for login and cart functionality.
📥 Setup Instructions
Prerequisites
- Python 3.11+ (Download)
- Chrome Browser (Latest version)
- PyCharm IDE (Recommended)
*Clone & Install Dependencies
- python -m venv .venv
- source .venv/bin/activate  # Linux/Mac
- .\.venv\Scripts\activate   # Windows
- pip install -r requirements.txt

Running the Tests
Command	Description
# Normal run
pytest
# With reports
pytest --html=reports/report.html

High Level Project Structure
saucedemo-tests/
├── .gitignore             # Specifies intentionally untracked files to ignore
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── pytest.ini             # Pytest configuration
├── conftest.py            # Pytest fixtures and hooks
│
├── features/              # BDD feature files
│   ├── login.feature      # Login scenarios in Gherkin
│   ├── cart.feature       # Shopping cart scenarios
│   └── steps/             # Step definition implementations
│       ├── __init__.py    # Makes steps a Python package
│       ├── login_steps.py # Login step definitions
│       └── cart_steps.py  # Cart step definitions
│
├── pages/                 # Page Object Model
│   ├── __init__.py        # Makes pages a Python package
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page elements and actions
│   ├── inventory_page.py  # Product inventory page
│   └── cart_page.py       # Shopping cart page
│
├── utils/                 # Utility functions
│   ├── browser.py         # Browser management utilities
│   └── helpers.py         # Common helper functions
│
├── drivers/               # WebDriver executables
│   └── chromedriver.exe   # ChromeDriver binary
│
├── reports/               # Test output
│   ├── html/              # HTML test reports
│   └── logs/              # Execution logs
│
└── tests/                 # Additional test modules (optional)
    ├── __init__.py
    └── unit/              # Unit tests (if applicable)



Happy Testing! 🚀