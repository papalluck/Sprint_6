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
    FAQ_ANSWER_1 = (By.XPATH, '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или")]')
    FAQ_ANSWER_2 = (By.XPATH, '//p[contains(text(),"Пока что у нас так: один заказ — один самокат. Есл")]')
    FAQ_ANSWER_3 = (By.XPATH, '//p[contains(text(),"Допустим, вы оформляете заказ на 8 мая. Мы привози")]')
    FAQ_ANSWER_4 = (By.XPATH, '//p[contains(text(),"Только начиная с завтрашнего дня. Но скоро станем")]')
    FAQ_ANSWER_5 = (By.XPATH, '//p[contains(text(),"Пока что нет! Но если что-то срочное — всегда можн")]')
    FAQ_ANSWER_6 = (By.XPATH, '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого х")]')
    FAQ_ANSWER_7 = (By.XPATH, '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, объ")]')
    FAQ_ANSWER_8 = (By.XPATH, '//p[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Моско")]')

    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//*[@id="root"]/div/div[1]/div[4]/div[2]/div[5]/button')
    # Куки
    COOKIES_BUTTON = (By.XPATH, '//button[@id="rcc-confirm-button"]')
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
        """Возвращает локатор для элемента станции метро в выпадающем списке."""
        return (By.XPATH, '//button[@value="1"]')

    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Вторая страница заказа
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    @staticmethod
    def delivery_date_day_locator(day):
        """Возвращает локатор для конкретного дня в календаре."""
        return (By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")

    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENTAL_PERIOD_DROPDOWN_CONTAINER = (By.XPATH, "//div[@class='Dropdown-menu']")  # Замените на правильный локатор контейнера!

    @staticmethod
    def rental_period_item_locator(rental_period_text):
        """Возвращает локатор для пункта выпадающего списка срока аренды."""
        return (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")

    SCOOTER_COLOR_BLACK = (By.XPATH, '//input[@id="black"]')
    SCOOTER_COLOR_GREY = (By.XPATH, '//input[@id="grey"]')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Подтверждение заказа
    CONFIRMATION_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS_BUTTON = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")
