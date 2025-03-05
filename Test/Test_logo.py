import pytest
import allure
from Pages.page_objects_main_page import MainPage
from urls import Urls
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



logger = logging.getLogger(__name__)


@allure.title('Проверка перехода на главную страницу')
class TestLogo:

    def setup(self):
        self.main_page = MainPage(self.driver)

    @pytest.fixture(autouse=True)
    def setup_class(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.wait = WebDriverWait(driver, 10)

        driver.get(Urls.BASE_URL)


    @allure.description('Тест проверки перехода на главную страницу Самоката по клику на логотип Самоката')
    def test_click_scooter_logo(self):
        logger.info("Кликаем на логотип самоката")
        self.main_page.click_scooter_logo()
        logger.info("Проверяем URL после клика на логотип")
        self.main_page.wait_url(Urls.BASE_URL)

    @allure.description('Тест проверки перехода на главную страницу Яндекса по клику на логотип Яндекса')
    def test_click_yandex_logo(self):
        logger.info("Кликаем на логотип Яндекса")
        main_window = self.driver.current_window_handle

        self.main_page.click_yandex_logo()

        logger.info("Переключаемся на новое окно")
        try:
            self.wait.until(EC.number_of_windows_to_be(2))

            new_window = [window for window in self.driver.window_handles if window != main_window][0]
            self.driver.switch_to.window(new_window)

            logger.info(f"Фактический URL после переключения: {self.driver.current_url}")

            self.main_page.wait_url("https://dzen.ru/")
        except Exception as e:
            logger.error(f"Ошибка при переключении на новое окно: {e}")
            raise

        finally:
            self.driver.switch_to.window(main_window)