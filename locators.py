from selenium.webdriver.common.by import By

class MainPageLocators:
    # Вопросы о важном
    FAQ_QUESTIONS_1 = (By.XPATH, '//*[@id="accordion__heading-0"]')
    FAQ_QUESTIONS_2 = (By.XPATH, '//*[@id="accordion__heading-1"]')
    FAQ_QUESTIONS_3 = (By.XPATH, '//*[@id="accordion__heading-2"]')
    FAQ_QUESTIONS_4 = (By.XPATH, '//*[@id="accordion__heading-3"]')
    FAQ_QUESTIONS_5 = (By.XPATH, '//*[@id="accordion__heading-4"]')
    FAQ_QUESTIONS_6 = (By.XPATH, '//*[@id="accordion__heading-5"]')
    FAQ_QUESTIONS_7 = (By.XPATH, '//*[@id="accordion__heading-6"]')
    FAQ_QUESTIONS_8 = (By.XPATH, '//*[@id="accordion__heading-7"]')

    # Ответы на вопросы
    FAQ_ANSWER_1 = (By.XPATH, '//div[@id="accordion__panel-0"]/p')
    FAQ_ANSWER_2 = (By.XPATH, '//div[@id="accordion__panel-1"]/p')
    FAQ_ANSWER_3 = (By.XPATH, '//div[@id="accordion__panel-2"]/p')
    FAQ_ANSWER_4 = (By.XPATH, '//div[@id="accordion__panel-3"]/p')
    FAQ_ANSWER_5 = (By.XPATH, '//div[@id="accordion__panel-4"]/p')
    FAQ_ANSWER_6 = (By.XPATH, '//div[@id="accordion__panel-5"]/p')
    FAQ_ANSWER_7 = (By.XPATH, '//div[@id="accordion__panel-6"]/p')
    FAQ_ANSWER_8 = (By.XPATH, '//div[@id="accordion__panel-7"]/p')

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]')

    # Куки
    COOKIES_BUTTON = (By.ID, "rcc-confirm-button")
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

class OrderPageLocators:
    # Первая страница заказа
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')

    @staticmethod
    def metro_station_item_locator(station_name):
        return (By.XPATH, '//button[@value="1"]')

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Вторая страница заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    @staticmethod
    def delivery_date_day_locator(day):
        return (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")

    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_DROPDOWN_CONTAINER = (By.XPATH, "//div[@class='Dropdown-menu']")

    @staticmethod
    def rental_period_item_locator(rental_period_text):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period_text}']")

    SCOOTER_COLOR_BLACK = (By.XPATH, '//input[@id="black"]')
    SCOOTER_COLOR_GREY = (By.XPATH, '//input[@id="grey"]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Подтверждение заказа
    CONFIRMATION_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")