import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging


logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logger

    @allure.step('Находит элемент {locator}')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Кликает на элемент {locator}')
    def click(self, locator):
        element = self.find_element(locator)
        try:
            self.driver.execute_script("arguments[0].click();", element)
            logger.info(f"Успешно кликнуто на элемент {locator} с помощью JavaScript")
        except Exception as e:
            logger.error(f"Не удалось кликнуть на элемент {locator}: {e}")
            raise

    @allure.step('Вводит текст "{text}" в элемент {locator}')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Прокручивает страницу до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)