from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PSTSignin:
    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # Signin Fields
    LOGIN_HEADER = (By.XPATH, '//h3[contains(text()="Login")]')
    EMAIL_FIELD = (By.XPATH, '//input[@data-test="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-submit"]')

    ERROR_MESSAGE = (By.XPATH, '//div[@data-test="login-error"]//div')

    def get_login_header(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOGIN_HEADER)
        )
        return element

    # From and To Field Methods
    def enter_email_field(self, email):
        # Enter From field
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def get_email_field_value(self):
        # Returns value of the From field
        return self.driver.find_element(*self.EMAIL_FIELD).get_attribute("value")

    def enter_password_field(self, password):
        # Enter To field
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def get_password_field_value(self):
        # Returns value of the To field
        return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("value")

    def click_login_button(self):
        # Click Login button
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        # Returns error message
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ERROR_MESSAGE)
        )
        return element

    # List of combined and unique methods
    def enter_login_info(self, email, password):
        self.enter_email_field(email)
        self.enter_password_field(password)