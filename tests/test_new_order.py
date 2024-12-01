import pytest

from data import OrderData
from locators.main_page_locators import HeadersButton
from locators.new_order_page_locators import AboutRentLocators
from page_objects.new_order_page import NewOrder


class TestNewOrder:

    @pytest.mark.parametrize(
        "button_locator, name, surname, address, phone, comment", OrderData.ORDER_DATA
    )
    def test_new_order(self, driver, button_locator, name, surname, address, phone, comment):
        new_order = NewOrder(driver)
        new_order.set_order(button_locator, name, surname, address, phone, comment)
        assert 'Заказ оформлен' in new_order.get_text_from_element(AboutRentLocators.TEXT_CONFIRMATION_OF_ORDER)
