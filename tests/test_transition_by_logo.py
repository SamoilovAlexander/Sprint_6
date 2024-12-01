from selenium.webdriver.support.wait import WebDriverWait

from data import Url
from locators.main_page_locators import HeadersButton
from page_objects.transition_by_logo import Headers


class TestTransitionByLogo:


    def test_transition_by_logo_scooter(self, driver):
        click_scooter = Headers(driver)
        new_url = click_scooter.click_logo_scooter()
        assert new_url == Url.URL_SCOOTER

    def test_transition_by_logo_yandex(self, driver):
        click_yandex = Headers(driver)
        click_yandex.click_logo_yandex()

        click_yandex.switch_to_new_window()
        new_url = click_yandex.get_url()
        assert Url.URL_DZEN in new_url
