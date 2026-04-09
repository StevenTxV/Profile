from selenium import webdriver
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # From and To Field
    FROM_FIELD_LOCATOR = (By.ID, 'from')
    TO_FIELD_LOCATOR = (By.ID, 'to')

    # Mode Options
    OPTIMAL_OPTION_LOCATOR = (By.XPATH, '//div[contains(@class, "mode") and text()="Optimal"]')
    FASTEST_OPTION_LOCATOR = (By.XPATH, '//div[contains(@class, "mode") and text()="Fastest"]')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[contains(@class, "mode") and text()="Custom"]')

    # Travel Icon Options
    CAR_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type")][1]/img[contains(@src, "car")]')
    WALK_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type")]/img[contains(@src, "walk")]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type")]/img[contains(@src, "taxi")]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type")]/img[contains(@src, "bike")]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type")]/img[contains(@src, "scooter")]')
    DRIVE_ICON_LOCATOR = (By.XPATH, '//div[contains(@class, "type drive")]/img[contains(@src, "car")]')

    # Selected Travel Information Section
    TRAVEL_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="duration"]')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Call a taxi"]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Book"]')

    # Plan Card Options
    BUSINESS_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][1]')
    SLEEPY_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][2]')
    HOLIDAY_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][3]')
    TALKING_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][4]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][5]')
    GLOSSY_PLAN_LOCATOR = (By.XPATH, '//div[@class="tariff-cards"]/div[contains(@class, "tcard")][6]')

    # Form Fields
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '//div[@class="np-text"]')
    PAYMENT_METHOD_BUTTON_LOCATOR = (By.XPATH, '//div[@class="pp-text"]')
    PAYMENT_METHOD_OPTION_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    MESSAGE_TO_THE_DRIVER_FIELD_LOCATOR = (By.ID, 'comment')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//button/span[text()="Order"]')

    # Order Requirements Fields
    BLANKET_AND_HANDKERCHIEFS_LOCATOR = (By.XPATH, '//div[@class="r r-type-switch"][1]//input')
    BLANKET_AND_HANDKERCHIEFS_OPTION_LOCATOR = (By.XPATH, '//div[@class="r r-type-switch"][1]//span')
    SOUNDPROOF_CURTAIN_OPTION_LOCATOR = (By.XPATH, '//div[@class="r r-type-switch"][2]//input')
    ICE_CREAM_VALUE_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][1]//div[@class="counter-value"]')
    ICE_CREAM_PLUS_BUTTON_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][1]//div[@class="counter-plus"]')
    CHOCOLATE_VALUE_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][2]//div[@class="counter-value"]')
    CHOCOLATE_PLUS_BUTTON_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][2]//div[@class="counter-plus"]')
    STRAWBERRY_VALUE_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][3]//div[@class="counter-value"]')
    STRAWBERRY_PLUS_BUTTON_LOCATOR = (By.XPATH, '//div[@class="r sub r-type-counter"][3]//div[@class="counter-plus"]')

    # Phone Number Popup Fields
    POPUP_PHONE_NUMBER_FIELD_LOCATOR = (By.ID, 'phone')
    POPUP_NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    POPUP_CODE_FIELD_LOCATOR = (By.ID, 'code')
    POPUP_CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')

    # Payment Method Popup Fields
    POPUP_ADD_CARD_LOCATOR = (By.XPATH, '//div[@class="pp-title" and text()="Add card"]')
    POPUP_TITLE_LOCATOR = (By.XPATH, '//div[@class="head" and text()="Adding a card"]')
    POPUP_CARD_NUMBER_FIELD_LOCATOR = (By.ID, 'number')
    POPUP_CARD_CODE_FIELD_LOCATOR = (By.XPATH, '//input[@id="code" and @class="card-input"]')
    POPUP_LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    POPUP_CLOSE_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"payment-picker")]//div[@class="section active"]/button')

    # Modal Popup Fields
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, '//div[@class="order-body"]')

    # List of Methods
    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    # From and To Field Methods
    def enter_from_field(self, from_text):
        # Enter From field
        self.driver.find_element(*self.FROM_FIELD_LOCATOR).send_keys(from_text)

    def get_from_field_value(self):
        # Returns value of the From field
        return self.driver.find_element(*self.FROM_FIELD_LOCATOR).get_attribute("value")

    def enter_to_field(self, to_text):
        # Enter To field
        self.driver.find_element(*self.TO_FIELD_LOCATOR).send_keys(to_text)

    def get_to_field_value(self):
        # Returns value of the To field
        return self.driver.find_element(*self.TO_FIELD_LOCATOR).get_attribute("value")

    # Travel Information Section Methods
    def click_call_a_taxi_button(self):
        # Clicks the Call a taxi button
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

    # Plan Card Option Methods
    def click_supportive_plan(self):
        # Clicks the Supportive plan
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def get_supportive_plan_class(self):
        # Returns the class of the supportive plan
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).get_attribute("class")

    # Form Field Section Methods
    def click_phone_number_field(self):
        # Clicks phone number field
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).click()

    def get_phone_number_field_text(self):
        # Returns the text of the phone number field
        return self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).text

    def click_payment_method_button(self):
        # Clicks payment method button
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON_LOCATOR).click()

    def get_payment_method_option_text(self):
        # Returns the text of the payment method option
        return self.driver.find_element(*self.PAYMENT_METHOD_OPTION_LOCATOR).text

    def enter_message_to_the_driver_field(self, comment):
        # Enters phone number in popup field
        self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_FIELD_LOCATOR).send_keys(comment)

    def get_message_to_the_driver_field_value(self):
        # Returns the value of the message to the driver field
        return self.driver.find_element(*self.MESSAGE_TO_THE_DRIVER_FIELD_LOCATOR).get_attribute("value")

    # Order Requirements Methods
    def click_blanket_and_handkerchiefs_option(self):
        # Clicks blanket and handkerchiefs option
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_OPTION_LOCATOR).click()

    def get_blanket_and_handkerchiefs_option_property(self):
        # Returns the property of the blanket and handkerchiefs option
        return self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_LOCATOR).get_property("checked")

    def click_ice_cream_plus_button(self):
        # Clicks the ice cream plus button
        self.driver.find_element(*self.ICE_CREAM_PLUS_BUTTON_LOCATOR).click()

    def get_ice_cream_value_text(self):
        # Returns the text of the ice cream value
        return self.driver.find_element(*self.ICE_CREAM_VALUE_LOCATOR).text

    def click_order_button(self):
        # Clicks Order button
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    # Popup Phone Number Methods
    def enter_popup_phone_number_field(self, phone_number):
        # Enters Phone Number in popup field
        self.driver.find_element(*self.POPUP_PHONE_NUMBER_FIELD_LOCATOR).send_keys(phone_number)

    def click_popup_next_button(self):
        # Clicks Next button in popup
        self.driver.find_element(*self.POPUP_NEXT_BUTTON_LOCATOR).click()

    def enter_popup_code_field(self, code):
        # Enters Code in popup field
        self.driver.find_element(*self.POPUP_CODE_FIELD_LOCATOR).send_keys(code)

    def click_popup_confirm_button(self):
        # Clicks Confirm button in popup
        self.driver.find_element(*self.POPUP_CONFIRM_BUTTON_LOCATOR).click()

    # Popup Card Methods
    def click_popup_add_card(self):
        # Clicks Add card in popup
        self.driver.find_element(*self.POPUP_ADD_CARD_LOCATOR).click()

    def click_popup_title(self):
        # Clicks title in popup
        self.driver.find_element(*self.POPUP_TITLE_LOCATOR).click()

    def enter_popup_card_number_field(self, card_number):
        # Enters Card Number field in popup field
        self.driver.find_element(*self.POPUP_CARD_NUMBER_FIELD_LOCATOR).send_keys(card_number)

    def enter_popup_card_code_field(self, card_code):
        # Enters Card Code in popup field
        self.driver.find_element(*self.POPUP_CARD_CODE_FIELD_LOCATOR).send_keys(card_code)

    def click_popup_link_button(self):
        # Clicks Link button in popup
        self.driver.find_element(*self.POPUP_LINK_BUTTON_LOCATOR).click()

    def click_popup_close_button(self):
        # Clicks Close button in popup
        self.driver.find_element(*self.POPUP_CLOSE_BUTTON_LOCATOR).click()

    # Modal Popup Field Methods
    def get_car_search_modal_displayed(self):
        # Returns true if the car search modal is displayed
        return self.driver.find_element(*self.CAR_SEARCH_MODAL_LOCATOR).is_displayed()

    # List of combined and unique methods
    def enter_addresses(self, from_text, to_text):
        self.enter_from_field(from_text)
        self.enter_to_field(to_text)

    def order_ice_cream(self, amount):
        for x in range(amount):
            # Add in S8
            self.click_ice_cream_plus_button()
            pass