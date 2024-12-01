from selenium.webdriver.common.by import By


class OrderFormLocators:
    FIELD_NAME = By.XPATH, '//html/body/div/div/div[2]/div[2]/div[1]/input'
    FIELD_SURNAME = By.XPATH, '//div[2]/div[2]/div[2]/input'
    FIELD_ADDRESS = By.XPATH, '//div[2]/div[2]/div[3]/input'
    FIELD_METRO_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    EXACT_METRO_STATION = By.XPATH, "//*[text()='Бульвар Рокоссовского']"
    FIELD_PHONE = By.XPATH, '//div[2]/div[2]/div[5]/input'
    BUTTON_NEXT = By.XPATH, './/div[2]/div[3]/button'

class AboutRentLocators:
    EXACT_RENT_PERIOD = By.XPATH, './/div[2]/div[2]/div[2]/div[2]/div[3]'
    NEW_MONTH = By.XPATH, '//html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/button[2]'
    EXACT_DATE = By.XPATH, '//html/body/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div[1]'
    FIELD_DATE_OF_BEGINING = By.XPATH, '//div/div/div[2]/div[2]/div[1]'
    FIELD_RENT_PERIOD = By.XPATH, './/div/div[2]/div[2]/div[2]'
    SUBFIELD_RENT_PERIOD = By.XPATH, '//div/div/div[2]/div[2]/div[2]/div[2]'
    FIELD_COLOUR_OF_SCOOTER = By.XPATH, '//div/div/div[2]/div[2]/div[3]/label[1]'
    FIELD_COMMENT = By.XPATH, '//div/div/div[2]/div[2]/div[4]/input'
    BUTTON_TO_FINISH_ORDER_UPPER = By.XPATH, './/div/div/div[1]/div[2]/button[1]'
    BUTTON_TO_FINISH_ORDER_LOWER = By.XPATH, './/div/div/div[2]/div[3]/button[2]'
    BUTTON_OF_CONFIRM_ORDER = By.XPATH, './/div/div/div[2]/div[5]/div[2]/button[2]'
    TEXT_CONFIRMATION_OF_ORDER = By.XPATH, '//div/div/div[2]/div[5]/div[1]'
    WATCH_STATUS = By.XPATH, '//div/div/div[2]/div[5]/div[2]/button'
