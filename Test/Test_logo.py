import pytest
import allure
from Pages.page_objects_main_page import MainPage
from urls import Urls
import logging


logger = logging.getLogger(__name__)

@allure.title('Проверка перехода на главную страницу')
class TestLogo:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)


    @allure.description('Тест проверки перехода на главную страницу Самоката по клику на логотип Самоката')
    def test_click_scooter_logo(self):
        logger.info("Кликаем на логотип самоката")
        self.main_page.click_scooter_logo()
        logger.info("Проверяем URL после клика на логотип")
        actual_url = self.main_page.get_current_url()
        assert actual_url == Urls.BASE_URL, f"Ожидаемый URL: {Urls.BASE_URL}, Фактический URL: {actual_url}"

    @allure.description('Тест проверки перехода на главную страницу Яндекса по клику на логотип Яндекса')
    def test_click_yandex_logo(self):
        logger.info("Кликаем на логотип Яндекса")
        main_window = self.driver.current_window_handle

        self.main_page.click_yandex_logo()

        logger.info("Переключаемся на новое окно")
        self.main_page.switch_to_new_window(main_window)

        logger.info("Ожидаем, пока URL не начнет содержать 'dzen.ru'")
        self.main_page.wait_for_url_contains("dzen.ru")

        logger.info(f"Фактический URL после переключения: {self.driver.current_url}")

        actual_url = self.main_page.get_current_url()
        assert "dzen.ru" in actual_url, f"Ожидаемый URL должен содержать 'dzen.ru', Фактический URL: {actual_url}"

        self.main_page.switch_to_main_window(main_window)