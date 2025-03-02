import pytest
import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderPageLocators
from locators import MainPageLocators
from selenium.webdriver.common.by import By
import time




class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_first_page(self, first_name, last_name, address, phone_number, metro_station_text):
        """Заполняет первую страницу формы заказа."""
        print("Заполняем поле Имя")
        first_name_input = self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name)
        print("Заполняем поле Фамилия")
        last_name_input = self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)
        print("Заполняем поле Адрес")
        address_input = self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT)
        address_input.send_keys(address)
        print("Заполняем поле Телефон")
        phone_number_input = self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_INPUT)
        phone_number_input.send_keys(phone_number)

        print("Кликаем по полю Метро")
        metro_station_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_station_input.click()
        print(f"Кликаем по станции: {metro_station_text}")
        metro_station_locator = OrderPageLocators.metro_station_item_locator(metro_station_text)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(metro_station_locator))
        metro_station_item = self.driver.find_element(*metro_station_locator)
        metro_station_item.click()
        print("Кликаем по кнопке Далее")
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_second_page(self, delivery_date, rental_period_text, color, comment):
        """Заполняет вторую страницу формы заказа, выбирая срок аренды."""

        print("Заполняем поле Дата доставки")
        delivery_date_input = self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_INPUT)
        delivery_date_input.send_keys(delivery_date)

        # Кликаем на любой день в календаре, чтобы закрыть его
        calendar_day = self.driver.find_element(By.XPATH,
                                                "//div[contains(@class, 'react-datepicker__day') and text()='1']")  # Кликаем на 1-е число
        calendar_day.click()
        time.sleep(1)  # Добавлено для проверки

        print("Кликаем по выпадающему списку 'Срок аренды'")
        rental_period_dropdown = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        try:
            # Явно ждем, пока элемент станет кликабельным
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
            )

            # Кликаем (пробуем стандартный клик)
            rental_period_dropdown.click()
            print("Кликнули по выпадающему списку 'Срок аренды'")
            time.sleep(1)  # Даем время на открытие списка
        except TimeoutException:
            print("Не удалось кликнуть по выпадающему списку 'Срок аренды'!")
            print("Текущий HTML:")
            print(self.driver.page_source)
            raise

        print("Ожидаем появления выпадающего списка 'Срок аренды'")
        try:
            # Ожидаем, пока контейнер появится и станет кликабельным
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded='true']"))
            )
            print("Выпадающий список 'Срок аренды' появился!")
        except TimeoutException:
            print("Выпадающий список 'Срок аренды' не появился вовремя!")
            print("Текущий HTML:")
            print(self.driver.page_source)
            raise  # Перебрасываем исключение

        print("Выбираем срок аренды: сутки")
        rental_period_item_locator = (
            By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")  # Используйте свой локатор
        try:
            # Явно ждем, пока элемент "сутки" станет кликабельным
            rental_period_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(rental_period_item_locator)
            )
            # Кликаем с помощью JavaScript
            self.driver.execute_script("arguments[0].click();", rental_period_item)
        except TimeoutException:
            print("Не удалось найти или кликнуть на элемент 'сутки' в выпадающем списке.")
            raise

        print(f"Выбираем цвет: {color}")
        if color == "black":
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()

        print("Заполняем поле Комментарий")
        comment_input = self.driver.find_element(*OrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(comment)
        print("Кликаем по кнопке Заказать")
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def confirm_order(self):
        """Подтверждает заказ."""
        print("Подтверждаем заказ")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRMATION_BUTTON)
        )
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_BUTTON).click()

    def get_order_success_message(self):
        """Получает текст сообщения об успешном заказе."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_STATUS_BUTTON)
        )
        return self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).text