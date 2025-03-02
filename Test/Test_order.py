import pytest
from selenium import webdriver
from Pages.page_objects_order_page import OrderPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Pages.page_objects_main_page import MainPage
from locators import OrderPageLocators
from locators import MainPageLocators
import allure
from urls import Urls


@allure.title('Проверка успешного оформления заказа')
class TestOrder:
    @allure.step('Открываем браузер Firefox')
    def setup_method(self, method):
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.get(Urls.BASE_URL)
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)

    @allure.step('Закрываем браузер')
    def teardown_method(self, method):
        self.driver.quit()

    @allure.description('Тест позитивного сценария заказа самоката.Проверяет: заполнение формы заказа,отображение кнопки статус заказа при успешном создании заказа,работу кнопок заказа (верхней и нижней)')
    @pytest.mark.parametrize("button_type", ["top", "bottom"])
    @pytest.mark.parametrize("first_name, last_name, address, phone_number, metro_station_text, delivery_date, rental_period_text, color, comment", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 10", "89001234567", "1", "01.01.2024", "1", "black", "Позвоните за час"),
        ("Петр", "Петров", "Санкт-Петербург, Невский пр., д. 20", "89117654321", "2", "05.01.2024", "2", "grey", "Домофон не работает")
    ])
    def test_order_scooter(self, button_type, first_name, last_name, address, phone_number, metro_station_text, delivery_date, rental_period_text, color, comment):

        print(f"Кликаем на кнопку 'Заказать' ({button_type})")
        self.main_page.click_order_button(button_type)

        print(f"Заполняем первую страницу: {first_name}, {last_name}, {address}, {phone_number}, {metro_station_text}")
        self.order_page.fill_first_page(first_name, last_name, address, phone_number, metro_station_text)

        print(f"Заполняем вторую страницу: {delivery_date}, {rental_period_text}, {color}, {comment}")
        self.order_page.fill_second_page(delivery_date, rental_period_text, color, comment)

        print("Подтверждаем заказ")
        self.order_page.confirm_order()

        print("Проверяем сообщение об успехе")
        success_message = self.order_page.get_order_success_message()
        print(f"Получено сообщение: {success_message}")
        assert "Посмотреть статус" in success_message, f"Ожидалось 'Посмотреть статус', но получено '{success_message}'"