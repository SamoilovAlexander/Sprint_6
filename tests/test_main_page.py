import pytest

from data import FAQData
from tests.conftest import driver
from page_objects.main_page import MainPage


class TestFAQ:

    @pytest.mark.parametrize('num, result', FAQData.ANSWERS)

    def test_FAQ(self, driver, num, result):
        main_page = MainPage(driver)
        actual = main_page.get_answer_text(num)
        assert actual == result
