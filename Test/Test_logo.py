from selenium import webdriver
from Pages.page_objects_order_page import OrderPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Pages.page_objects_main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from urls import Urls

@allure.title('Проверка логотипов «Самоката» и «Яндекса»')
class TestLogo:
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

    @allure.description('Тест проверки перехода на главную страницу по клику на логотип «Самоката»')
    def test_click_scooter_logo(self):

        print("Кликаем на логотип «Самоката»")

        self.main_page.click_scooter_logo()

        print("Проверяем, что перешли на главную страницу")
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("qa-scooter.praktikum-services.ru")
        )
        assert "qa-scooter.praktikum-services.ru" in self.driver.current_url, \
            "Не удалось перейти на главную страницу по клику на логотип самоката"

    @allure.description('Тест проверки перехода на главную страницу Яндекса по клику на логотип Яндекса')
    def test_click_yandex_logo(self):

        print("Кликаем на логотип Яндекса")
        main_window = self.driver.current_window_handle

        self.main_page.click_yandex_logo()

        print("Переключаемся на новое окно")
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        print("Проверяем, что открылась главная страница Дзена")
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
        assert "dzen.ru" in self.driver.current_url, "Не удалось перейти на главную страницу Дзена"

        print("Закрываем новое окно и переключаемся обратно на основное")
        self.driver.close()
        self.driver.switch_to.window(main_window)