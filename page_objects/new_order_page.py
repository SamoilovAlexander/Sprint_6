from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import NewOrderLocators, AgreeCookies
from locators.new_order_page_locators import OrderFormLocators, AboutRentLocators
from page_objects.base_page import BasePage


class NewOrder(BasePage):

    def set_order(self, order_button_locator, name, surname, address, phone, comment):
        self.scroll_to_element(order_button_locator)
        self.click_to_element(order_button_locator)
        self.click_to_element(AgreeCookies.COOKIE_AGREE)
        self.add_text_to_element(OrderFormLocators.FIELD_NAME, name)
        self.add_text_to_element(OrderFormLocators.FIELD_SURNAME, surname)
        self.add_text_to_element(OrderFormLocators.FIELD_ADDRESS, address)
        self.click_to_element(OrderFormLocators.FIELD_METRO_STATION)
        self.click_to_element(OrderFormLocators.EXACT_METRO_STATION)
        self.add_text_to_element(OrderFormLocators.FIELD_PHONE, phone)
        self.click_to_element(OrderFormLocators.BUTTON_NEXT)
        self.click_to_element(AboutRentLocators.FIELD_DATE_OF_BEGINING)
        self.click_to_element(AboutRentLocators.EXACT_DATE)
        self.click_to_element(AboutRentLocators.FIELD_RENT_PERIOD)
        self.click_to_element(AboutRentLocators.EXACT_RENT_PERIOD)
        self.click_to_element(AboutRentLocators.FIELD_COLOUR_OF_SCOOTER)
        self.add_text_to_element(AboutRentLocators.FIELD_COMMENT, comment)
        self.click_to_element(AboutRentLocators.BUTTON_TO_FINISH_ORDER_LOWER)
        self.click_to_element(AboutRentLocators.BUTTON_OF_CONFIRM_ORDER)

    def switch_to(self, param):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes('https://dzen.ru/?yredirect=true'))
        self.driver.switch_to(param)

