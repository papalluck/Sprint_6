import pytest
import allure
from selenium.common import TimeoutException
from Pages.page_objects_main_page import MainPage
from Pages.page_objects_order_page import OrderPage
from urls import Urls
import logging
from selenium.webdriver.support import expected_conditions as EC
logger = logging.getLogger(__name__)
from base_page import BasePage

@allure.title('Проверка логотипов «Самоката» и «Яндекса»')
class TestLogo:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.driver.get(Urls.BASE_URL)

    @allure.description('Тест проверки перехода на главную страницу по клику на логотип «Самоката»')
    def test_click_scooter_logo(self,):
        logger.info("Кликаем на логотип «Самоката»")
        self.main_page.click_scooter_logo()

        logger.info("Проверяем, что перешли на главную страницу")
        try:
            assert Urls.BASE_URL in self.driver.current_url, "Не удалось перейти на главную страницу по клику на логотип самоката"
        except Exception as e:
            logger.error(f"Ошибка при проверке перехода на главную страницу: {e}")
            raise

    @allure.description('Тест проверки перехода на главную страницу Яндекса по клику на логотип Яндекса')
    def test_click_yandex_logo(self):
        logger.info("Кликаем на логотип Яндекса")
        main_window = self.driver.current_window_handle

        self.main_page.click_yandex_logo()

        logger.info("Переключаемся на новое окно")
        try:
            self.wait.until(EC.number_of_windows_to_be(2)) # используем wait из BasePage
        except TimeoutException:
            logger.error("Не удалось дождаться открытия нового окна")
            raise

        for handle in self.driver.window_handles:
            if handle != main_window:
                self.driver.switch_to.window(handle)
                break

        logger.info("Проверяем, что открылась главная страница Дзена")
        try:
            self.wait.until(EC.url_contains("dzen.ru")) # используем wait из BasePage
            assert "dzen.ru" in self.driver.current_url, "Не удалось перейти на главную страницу Дзена"
        except Exception as e:
            logger.error(f"Ошибка при проверке перехода на главную страницу Дзена: {e}")
            raise

        logger.info("Закрываем новое окно и переключаемся обратно на основное")
        self.driver.close()
        self.driver.switch_to.window(main_window)