import pytest
from selenium import webdriver

from data import Url


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.URL_SCOOTER)
    yield driver
    driver.quit()
