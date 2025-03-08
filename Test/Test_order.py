import pytest
from Pages.page_objects_order_page import OrderPage
from Pages.page_objects_main_page import MainPage
import allure
from urls import Urls
import logging
from locators import OrderPageLocators

logger = logging.getLogger(__name__)

@allure.title('Проверка успешного оформления заказа')
class TestOrder:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.driver.get(Urls.BASE_URL)

    @allure.description('Тест позитивного сценария заказа самоката. Проверяет: заполнение формы заказа, отображение кнопки статус заказа, работу кнопок заказа (верхней и нижней)')
    @pytest.mark.parametrize("button_type", ["top", "bottom"])
    @pytest.mark.parametrize("first_name, last_name, address, phone_number, metro_station_text, delivery_date, rental_period_text, color, comment", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 10", "89001234567", "Бульвар Рокоссовского", "01.01.2024", "сутки", "black", "Позвоните за час"),
        ("Петр", "Петров", "Санкт-Петербург, Невский пр., д. 20", "89117654321", "Черкизовская", "05.01.2024", "двое суток", "grey", "Домофон не работает")
    ])
    def test_order_scooter(self, driver, button_type, first_name, last_name, address, phone_number, metro_station_text, delivery_date, rental_period_text, color, comment):
        logger.info(f"Начинаем тест заказа самоката с кнопкой: {button_type}, {first_name}, {last_name}")

        logger.info(f"Кликаем на кнопку 'Заказать' ({button_type})")
        self.main_page.click_order_button(button_type)

        logger.info(f"Заполняем первую страницу: {first_name}, {last_name}, {address}, {phone_number}, {metro_station_text}")
        metro_station_locator = OrderPageLocators.metro_station_item_locator(metro_station_text)
        self.order_page.fill_first_page(first_name, last_name, address, phone_number, metro_station_locator)

        logger.info(f"Заполняем вторую страницу: {delivery_date}, {rental_period_text}, {color}, {comment}")
        self.order_page.fill_second_page(delivery_date, rental_period_text, color, comment)

        logger.info("Подтверждаем заказ")
        self.order_page.confirm_order()

        logger.info("Проверяем сообщение об успехе")
        success_message = self.order_page.get_order_success_message()
        logger.info(f"Получено сообщение: {success_message}")
        assert "Посмотреть статус" in success_message, f"Ожидалось 'Посмотреть статус', но получено '{success_message}'"