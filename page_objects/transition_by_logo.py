from locators.main_page_locators import HeadersButton, NewOrderLocators
from page_objects.base_page import BasePage


class Headers(BasePage):
    def click_logo_scooter(self):
        self.click_to_element(NewOrderLocators.BUTTON_TO_START_ORDER_UPPER)
        self.click_to_element(HeadersButton.LOGO_SCOOTER)
        return self.get_url()

    def click_logo_yandex(self):
        self.click_to_element(HeadersButton.LOGO_YANDEX)
        return self.get_url()

    def check_dzen_logo(self):
        self.find_element_with_wait(HeadersButton.YANDEX_SEARCH)
        return self.get_url()
