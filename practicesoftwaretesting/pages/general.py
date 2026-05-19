from selenium import webdriver
from selenium.webdriver.common.by import By

class PSTGeneral:
    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # Header
    HOME_BUTTON = (By.XPATH, '//a[@data-test="nav-home"]')
    CATEGORIES_DROPDOWN = (By.XPATH, '//a[@data-test="nav-categories"]')
    CONTACT_BUTTON = (By.XPATH, '//a[@data-test="nav-contact"]')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@data-test="nav-sign-in"]')

    PROFILE_BUTTON = (By.XPATH, '//a[@data-test="nav-menu"]')
    SIGN_OUT_BUTTON = (By.XPATH, '//a[@data-test="nav-sign-out"]')

    # Header Methods
    def click_home_button(self):
        # Click Home button
        self.driver.find_element(*self.HOME_BUTTON).click()

    def click_sign_in_button(self):
        # Click Sign in button
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def click_profile_button(self):
        # Click profile button
        self.driver.find_element(*self.PROFILE_BUTTON).click()

    def click_sign_out_button(self):
        # Click sign out button
        self.driver.find_element(*self.SIGN_OUT_BUTTON).click()

    def logout(self):
        self.click_profile_button()
        self.click_sign_out_button()