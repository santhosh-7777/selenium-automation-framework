import pytest
import csv
from pages.login_page import LoginPage

def load_data():
    data = []
    with open("data/test_data.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append((row["username"], row["password"], row["expected"]))
    return data

class TestDataDriven:
    @pytest.mark.parametrize("username,password,expected", load_data())
    def test_login_data_driven(self, driver, username, password, expected):
        page = LoginPage(driver)
        page.open()
        page.login(username, password)

        if expected == "pass":
            import time
            time.sleep(3)
            assert "dashboard" in driver.current_url.lower()
        else:
            assert "dashboard" not in driver.current_url.lower()