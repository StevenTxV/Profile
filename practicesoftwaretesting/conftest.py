import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("unsupported browser")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()