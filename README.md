# Selenium Automation Framework

A production-ready end-to-end test automation framework built with Python and Selenium WebDriver, following industry-standard design patterns used in real QA engineering roles.

## Tech Stack

- Python 3.13
- Selenium WebDriver 4.44
- Pytest
- Allure Reports
- GitHub Actions (CI/CD)
- Page Object Model (POM)

## Project Structure
selenium-automation-framework/
├── pages/
│   ├── base_page.py          # Common reusable actions
│   └── login_page.py         # Login page elements and actions
├── tests/
│   ├── test_login.py         # Login functional test cases
│   └── test_data_driven.py   # Data-driven test cases
├── utils/
│   └── driver_factory.py     # Chrome WebDriver setup
├── data/
│   └── test_data.csv         # External test data
├── reports/                  # Generated HTML and Allure reports
├── screenshots/              # Auto-captured on test failure
├── conftest.py               # Pytest fixtures and hooks
├── pytest.ini                # Pytest configuration
└── requirements.txt          # Project dependencies

## Features

- Page Object Model design pattern for maintainable and scalable test code
- Data-driven testing using external CSV files
- Automatic screenshot capture on test failure
- Allure report generation with full test execution details
- HTML report generation after every test run
- CI/CD pipeline via GitHub Actions that runs tests on every push
- Headless Chrome execution on cloud environments

## Test Cases Covered

Login functionality on OrangeHRM demo application:

- Valid login with correct credentials
- Invalid login with wrong password
- Invalid login with wrong username
- Login attempt with empty credentials
- Data-driven login with 5 different credential combinations

## Setup and Installation

1. Clone the repository

git clone https://github.com/santhosh-7777/selenium-automation-framework.git
cd selenium-automation-framework

2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

## Running Tests

Run all tests:

pytest tests/ -v

Run with HTML report:

pytest tests/ -v --html=reports/report.html

Run with Allure report:

pytest tests/ --alluredir=reports/allure-results -v
allure serve reports/allure-results

## CI/CD

This project uses GitHub Actions to automatically run the full test suite on every push to the main branch. Results are visible under the Actions tab of this repository.

## Application Under Test

OrangeHRM Demo: https://opensource-demo.orangehrmlive.com