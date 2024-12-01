from selenium.webdriver.common.by import By


class OrderFormLocators:
    FIELD_NAME = By.XPATH, './/input[@placeholder="* Имя"]'
    FIELD_SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'
    FIELD_ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    FIELD_METRO_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    EXACT_METRO_STATION = By.XPATH, "//*[text()='Бульвар Рокоссовского']"
    FIELD_PHONE = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    BUTTON_NEXT = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

class AboutRentLocators:
    FIELD_DATE_OF_BEGINING = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]'
    NEW_MONTH = By.XPATH, './/*[@class="react-datepicker__navigation react-datepicker__navigation--next"]'
    EXACT_DATE = By.XPATH, './/*[@class="react-datepicker__day react-datepicker__day--012"]'


    FIELD_RENT_PERIOD = By.XPATH, './/*[@class="Dropdown-placeholder"]'
    EXACT_RENT_PERIOD = By.XPATH, './/*[contains(text(), "четверо суток")]'


    FIELD_COLOUR_OF_SCOOTER = By.XPATH, './/*[contains(@id, "black")]'
    FIELD_COMMENT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    BUTTON_TO_FINISH_ORDER_UPPER = By.XPATH, './/button[@class="Button_Button__ra12g"]'
    BUTTON_TO_FINISH_ORDER_LOWER = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    BUTTON_OF_CONFIRM_ORDER = By.XPATH, './/button[contains(text(), "Да")]'
    TEXT_CONFIRMATION_OF_ORDER = By.XPATH, './/*[contains(text(), "Заказ оформлен")]'
    WATCH_STATUS = By.XPATH, '//*button[contains(text(), "Посмотреть статус")]'
