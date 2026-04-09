import data
import helpers
from pages import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

        # Checks if server is on
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Ensure that users can correctly set pickup and destination addresses and that they are properly recorded.
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Assert From and To fields
        actual_from_value = urban_routes_page.get_from_field_value()
        actual_to_value = urban_routes_page.get_to_field_value()
        assert data.ADDRESS_FROM == actual_from_value, f"Expected '{data.ADDRESS_FROM}', but got '{actual_from_value}'"
        assert data.ADDRESS_TO == actual_to_value, f"Expected '{data.ADDRESS_TO}', but got '{actual_to_value}'"

    # Ensure users can choose the Supportive plan and validate their selection without hardcoding values.
    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Assert supportive plan is selected
        actual_value = urban_routes_page.get_supportive_plan_class()
        expected_value = "active"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Ensure that users can enter their phone number, receive a confirmation SMS code, and validate their login.
    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Enter phone number
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_popup_phone_number_field(data.PHONE_NUMBER)
        urban_routes_page.click_popup_next_button()
        urban_routes_page.enter_popup_code_field(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_popup_confirm_button()

        # Assert phone numbers are equal
        actual_value = urban_routes_page.get_phone_number_field_text()
        expected_value = data.PHONE_NUMBER
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"


    # Verify that users can add a valid credit card and that the "Link" button becomes clickable only after a valid input.
    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Add payment option
        urban_routes_page.click_payment_method_button()
        urban_routes_page.click_popup_add_card()
        urban_routes_page.enter_popup_card_number_field(data.CARD_NUMBER)
        urban_routes_page.enter_popup_card_code_field(data.CARD_CODE)
        urban_routes_page.click_popup_title()
        urban_routes_page.click_popup_link_button()
        urban_routes_page.click_popup_close_button()

        # Assert payment option was changed
        actual_value = urban_routes_page.get_payment_method_option_text()
        expected_value = "Card"
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Ensure that users can leave a comment for the driver before confirming the order.
    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Enter comment in field
        urban_routes_page.enter_message_to_the_driver_field(data.MESSAGE_FOR_DRIVER)

        # Assert comments are equal
        actual_value = urban_routes_page.get_message_to_the_driver_field_value()
        expected_value = data.MESSAGE_FOR_DRIVER
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Ensure users can order additional items and that they are properly displayed.
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Clicks the blanket and handkerchief toggle
        urban_routes_page.click_blanket_and_handkerchiefs_option()

        # Assert blanket and handkerchief toggle is on
        actual_value = urban_routes_page.get_blanket_and_handkerchiefs_option_property()
        assert actual_value, f"Expected True, but got '{actual_value}'"

    # Ensure that selecting 2 ice creams is reflected on the screen.
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Adds ice cream
        urban_routes_page.order_ice_cream(data.ICE_CREAM_AMOUNT)

        # Assert ice cream amount is equal to data.ICE_CREAM_AMOUNT
        actual_value = urban_routes_page.get_ice_cream_value_text()
        expected_value = str(data.ICE_CREAM_AMOUNT)
        assert expected_value == actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Verify that selecting the Supportive tariff correctly triggers the car search process.
    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Enter addresses
        urban_routes_page.enter_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)

        # Clicks call a taxi button and the supportive plan
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan()

        # Enter phone number
        urban_routes_page.click_phone_number_field()
        urban_routes_page.enter_popup_phone_number_field(data.PHONE_NUMBER)
        urban_routes_page.click_popup_next_button()
        urban_routes_page.enter_popup_code_field(helpers.retrieve_phone_code(self.driver))
        urban_routes_page.click_popup_confirm_button()

        # Enter message
        urban_routes_page.enter_message_to_the_driver_field(data.MESSAGE_FOR_DRIVER)

        # Click the order button
        urban_routes_page.click_order_button()

        # Assert modal is displayed
        actual_value = urban_routes_page.get_car_search_modal_displayed()
        assert actual_value, f"Expected True, but got '{actual_value}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()