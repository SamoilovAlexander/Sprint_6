from data import Url
from page_objects.transition_by_logo import Headers
from tests.conftest import driver


class TestTransitionByLogo:


    def test_transition_by_logo_scooter(self, driver):
        click_scooter = Headers(driver)
        new_url = click_scooter.click_logo_scooter()
        assert new_url == Url.URL_SCOOTER

    def test_transition_by_logo_yandex(self, driver):
        click_yandex = Headers(driver)
        click_yandex.click_logo_yandex()
        click_yandex.switch_to_new_window()

        driver.implicitly_wait(5)
        new_url = driver.current_url
        assert Url.URL_DZEN in new_url
