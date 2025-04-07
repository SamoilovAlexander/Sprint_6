from selenium.webdriver.common.by import By

class AgreeCookies:
    COOKIE_AGREE = By.XPATH, '//*[@id="rcc-confirm-button"]'

class FAQLocators: #общие локаторы вопросов и ответов
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'
    SCROLL_TO_THE_LAST_QUESTION = By.XPATH, '//*[@id="accordion__heading-7"]'

class NewOrderLocators:
    BUTTON_TO_START_ORDER_UPPER = By.XPATH, './/button[@class="Button_Button__ra12g"]'
    BUTTON_TO_START_ORDER_LOWER = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

class HeadersButton:
    LOGO_SCOOTER = By.XPATH, '//*[@class="Header_LogoScooter__3lsAR"]'
    LOGO_YANDEX = By.XPATH, '//*[@class="Header_LogoYandex__3TSOI"]'
    SCOOTER_SLOGAN = By.XPATH, '//*[@class="Home_SubHeader__zwi_E"]'
    YANDEX_SEARCH = By.XPATH, './/button[@text="Найти"]'
    DZEN_MAIN = By.XPATH, '//[@class="dzen-layout--navigation-tab__text-2g"]'
    HEADER_DZEN = By.ID, "dzen-header"
