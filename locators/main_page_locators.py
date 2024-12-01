from selenium.webdriver.common.by import By

class AgreeCookies:
    COOKIE_AGREE = By.XPATH, '//*[@id="rcc-confirm-button"]'

class FAQLocators: #общие локаторы вопросов и ответов
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    SCROLL_TO_THE_LAST_QUESTION = By.XPATH, '//*[@id="accordion__heading-7"]'

class NewOrderLocators:
    BUTTON_TO_START_ORDER_UPPER = By.XPATH, '//div/div/div/div[1]/div[2]/button[1]'
    BUTTON_TO_START_ORDER_LOWER = By.XPATH, '//div/div/div/div[4]/div[2]/div[5]/button'

class HeadersButton:
    LOGO_SCOOTER = By.XPATH, './/a[2]/img'
    LOGO_YANDEX = By.XPATH, './/a[1]/img'
    SCOOTER_SLOGAN = By.XPATH, '//div/div/div/div[2]/div[4]/div[1]'
    YANDEX_SEARCH = By.XPATH, './/body/form/button[@text="Найти"]'
    DZEN_MAIN = By.XPATH, './/div[13]/div/div[2]/div[1]/aside/ul/a[1]/li/div/div[1]/svg'
    HEADER_DZEN = By.ID, "dzen-header"
