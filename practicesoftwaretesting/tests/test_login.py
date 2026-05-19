from data import data
from utils import helpers
from pages.general import PSTGeneral
from pages.myaccount import PSTMyAccount
from pages.signin import PSTSignin
from selenium import webdriver


# Ensure that users can correctly log into the application with valid credentials.
def test_login_1(driver):
    driver.get(data.URL_HOME)
    general_page = PSTGeneral(driver)
    signin_page = PSTSignin(driver)
    myaccount_page = PSTMyAccount(driver)

    # Navigate to Signin page
    general_page.click_sign_in_button()

    # Enter data into fields
    signin_page.enter_login_info(data.EMAIL_ADDRESS, data.PASSWORD)
    signin_page.click_login_button()

    # Assert Account page exists
    element = myaccount_page.get_account_header()
    assert element.is_displayed(), f"Account page header does not exist."

# Ensure that users can fail to log into the application with invalid password.
def test_login_2(driver):
    driver.get(data.URL_HOME)
    general_page = PSTGeneral(driver)
    signin_page = PSTSignin(driver)
    myaccount_page = PSTMyAccount(driver)

    # Navigate to Signin page
    general_page.click_sign_in_button()

    # Enter data into fields
    signin_page.enter_login_info(data.EMAIL_ADDRESS, "wrongpass")
    signin_page.click_login_button()

    # Assert Account page exists
    element = signin_page.get_error_message()
    assert element.is_displayed(), f"Error message is not displayed."
    assert element.text == "Invalid email or password", f"Error message does not exist."