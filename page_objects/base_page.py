from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from socks import method


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1 # '//*[@class="my-question-locator-{}"]'
        locator = locator.format(num) # '//*[@class="my-question-locator-1"]'
        return (method, locator)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
