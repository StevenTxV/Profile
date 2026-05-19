from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PSTMyAccount:
    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # My Account page
    MY_ACCOUNT_HEADER = (By.XPATH, '//h1[@data-test="page-title"]')

    # Header Methods
    def get_account_header(self):
        # Find account_header
        element =  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MY_ACCOUNT_HEADER)
        )
        return element