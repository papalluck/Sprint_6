import allure
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logger = logging.getLogger(__name__)

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logger

    @allure.step('Находит элемент {locator} в течение {time} секунд')
    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Не удалось найти элемент {locator} за {time} секунд"
            )
            self.logger.info(f"Успешно найден элемент {locator}")
            return element
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элемента {locator}: {e}")
            raise

    def find_elements(self, locator, time=10):
        try:
            elements = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Не удалось найти элементы {locator} за {time} секунд"
            )
            self.logger.info(f"Успешно найдены элементы {locator}")
            return elements
        except Exception as e:
            self.logger.error(f"Ошибка при поиске элементов {locator}: {e}")
            raise

    @allure.step('Ожидает кликабельности элемента {locator} в течение {time} секунд')
    def wait_for_clickable(self, locator, time=10, message=""):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator),
                message=message
            )
            self.logger.info(f"Элемент {locator} стал кликабельным")
            return element
        except Exception as e:
            self.logger.error(f"Ошибка при ожидании кликабельности элемента {locator}: {e}")
            raise

    def wait_for_visible(self, locator, time=10, message=""):
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.visibility_of_element_located(locator),
                message=f"Элемент {locator} не стал видимым за {time} секунд"
            )
            self.logger.info(f"Элемент {locator} стал видимым")
            return element
        except Exception as e:
            self.logger.error(f"Ошибка при ожидании видимости элемента {locator}: {e}")
            raise

    @allure.step('Кликает на элемент {locator}')
    def click(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.info(f"Успешно кликнули на элемент {locator}")
        except Exception as e:
            self.logger.error(f"Не удалось кликнуть на элемент {locator}: {e}")
            raise

    @allure.step('Вводит текст "{text}" в элемент {locator}')
    def send_keys(self, locator, text):
        try:
            element = self.find_element(locator)
            element.send_keys(text)
            self.logger.info(f"Успешно введён текст '{text}' в элемент {locator}")
        except Exception as e:
            self.logger.error(f"Не удалось ввести текст '{text}' в элемент {locator}: {e}")
            raise

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.logger.info(f"Успешно прокручено до элемента {locator}")
        except Exception as e:
            self.logger.error(f"Не удалось прокрутить до элемента {locator}: {e}")
            raise

    def get_text(self, locator):
        try:
            element = self.find_element(locator)
            text = element.text
            self.logger.info(f"Успешно получен текст элемента {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Не удалось получить текст элемента {locator}: {e}")
            raise

    def clear(self, locator):
        try:
            element = self.find_element(locator)
            element.clear()
            self.logger.info(f"Успешно очищено поле {locator}")
        except Exception as e:
            self.logger.error(f"Не удалось очистить поле {locator}: {e}")
            raise

    def get_attribute(self, locator, attribute):
        try:
            element = self.find_element(locator)
            value = element.get_attribute(attribute)
            self.logger.info(f"Успешно получен атрибут '{attribute}' элемента {locator}: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Не удалось получить атрибут '{attribute}' элемента {locator}: {e}")
            raise

    def wait_url_contains(self, url, timeout=20):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(url),
                message=f"Не удалось дождаться URL, содержащего '{url}'"
            )
            self.logger.info(f"Успешно дождались URL, содержащего '{url}'")
        except Exception as e:
            self.logger.error(f"Не удалось дождаться URL, содержащего '{url}': {e}")
            raise

    def switch_to_new_window(self, main_window_handle, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            new_window = [window for window in self.driver.window_handles if window != main_window_handle][0]
            self.driver.switch_to.window(new_window)
            self.logger.info("Успешно переключились на новое окно")
        except Exception as e:
            self.logger.error(f"Не удалось переключиться на новое окно: {e}")
            raise

    def switch_to_main_window(self, main_window_handle):
        try:
            self.driver.switch_to.window(main_window_handle)
            self.logger.info("Успешно вернулись в основное окно")
        except Exception as e:
            self.logger.error(f"Не удалось вернуться в основное окно: {e}")
            raise

    def get_current_url(self):
        try:
            url = self.driver.current_url
            self.logger.info(f"Успешно получили текущий URL: {url}")
            return url
        except Exception as e:
            self.logger.error(f"Не удалось получить текущий URL: {e}")
            raise

    @allure.step('Ожидает кликабельности элемента {locator} и кликает на него')
    def wait_and_click(self, locator, time=10, message=""):
        try:
            element = self.wait_for_clickable(locator, time, message)
            self.click(locator)
            self.logger.info(f"Успешно дождались кликабельности элемента {locator} и кликнули на него")
            return element
        except Exception as e:
            self.logger.error(f"Не удалось дождаться кликабельности элемента {locator} и кликнуть на него: {e}")
            raise