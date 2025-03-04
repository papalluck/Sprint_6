import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import OrderPageLocators
from base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Заполняем первую страницу формы заказа')
    def fill_first_page(self, first_name, last_name, address, phone_number, metro_station_text):
        self.logger.info("Заполняем первую страницу формы заказа")
        self._fill_input(OrderPageLocators.FIRST_NAME_INPUT, first_name, "Имя")
        self._fill_input(OrderPageLocators.LAST_NAME_INPUT, last_name, "Фамилия")
        self._fill_input(OrderPageLocators.ADDRESS_INPUT, address, "Адрес")
        self._fill_input(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number, "Телефон")

        self.logger.info("Кликаем по полю Метро")
        metro_station_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        self.click(OrderPageLocators.METRO_STATION_INPUT)

        self.logger.info(f"Кликаем по станции: {metro_station_text}")
        metro_station_locator = OrderPageLocators.metro_station_item_locator(metro_station_text)
        self.click(metro_station_locator)

        self.logger.info("Кликаем по кнопке Далее")
        self.click(OrderPageLocators.NEXT_BUTTON)

    def _fill_input(self, locator, value, field_name):
         self.logger.info(f"Заполняем поле {field_name}")
         input_element = self.find_element(locator)
         input_element.send_keys(value)

    @allure.step('Заполняем вторую страницу формы заказа, выбирая срок аренды')
    def fill_second_page(self, delivery_date, rental_period_text, color, comment):

        self.logger.info("Заполняем вторую страницу формы заказа")

        self.logger.info("Заполняем поле Дата доставки")
        delivery_date_input = self.find_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        delivery_date_input.send_keys(delivery_date)

        self.logger.info("Кликаем на любой день в календаре, чтобы закрыть его")
        calendar_day_locator = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='1']")
        self.click(calendar_day_locator)

        self.logger.info("Кликаем по выпадающему списку 'Срок аренды'")
        rental_period_dropdown = self.find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        try:
            self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
            self.logger.info("Кликнули по выпадающему списку 'Срок аренды'")

        except TimeoutException:
            self.logger.exception("Не удалось кликнуть по выпадающему списку 'Срок аренды'!")
            self.logger.debug(f"Текущий HTML:\n{self.driver.page_source}")
            raise

        self.logger.info("Ожидаем появления выпадающего списка 'Срок аренды'")
        try:
            dropdown_locator = (By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded='true']")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(dropdown_locator)
            )
            self.logger.info("Выпадающий список 'Срок аренды' появился!")
        except TimeoutException:
            self.logger.exception("Выпадающий список 'Срок аренды' не появился вовремя!")
            self.logger.debug(f"Текущий HTML:\n{self.driver.page_source}")
            raise

        self.logger.info("Выбираем срок аренды: сутки")
        rental_period_item_locator = (
            By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
        try:
            rental_period_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(rental_period_item_locator)
            )
            self.driver.execute_script("arguments[0].click();", rental_period_item)
        except TimeoutException:
            self.logger.exception("Не удалось найти или кликнуть на элемент 'сутки' в выпадающем списке.")
            raise

        self.logger.info(f"Выбираем цвет: {color}")
        if color == "black":
            self.click(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.SCOOTER_COLOR_GREY)

        self.logger.info("Заполняем поле Комментарий")
        comment_input = self.find_element(OrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(comment)
        self.logger.info("Кликаем по кнопке Заказать")
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.logger.info("Подтверждаем заказ")
        self.click(OrderPageLocators.CONFIRMATION_BUTTON)

    @allure.step('Получаем текст сообщения об успешном заказе')
    def get_order_success_message(self):
        self.logger.info("Получаем текст сообщения об успешном заказе.")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_STATUS_BUTTON)
        )
        return self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).text