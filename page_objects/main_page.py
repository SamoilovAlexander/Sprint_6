from locators.main_page_locators import FAQLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):


    def get_answer_text(self, num):
        locator_q_formatted = self.format_locators(FAQLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(FAQLocators.ANSWER_LOCATOR, num)
        self.scroll_to_element(FAQLocators.SCROLL_TO_THE_LAST_QUESTION)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

