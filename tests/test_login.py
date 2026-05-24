import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("Admin", "admin123")
        assert "dashboard" in driver.current_url.lower()

    def test_invalid_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("Admin", "wrongpass")
        error = page.get_error()
        assert "Invalid credentials" in error

    def test_invalid_username(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("wronguser", "admin123")
        error = page.get_error()
        assert "Invalid credentials" in error

    def test_empty_credentials(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("", "")
        assert "dashboard" not in driver.current_url.lower()