import logging
import EC
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

    @allure.step('Находит элемент на странице')
    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            self.logger.exception(f"Не удалось найти элемент по локатору {locator}")
            raise

    @allure.step('Кликает на элемент')
    def click(self, locator, time=10):
        element = self.find_element(locator, time)
        try:
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException:
            self.logger.exception(f"Не удалось кликнуть на элемент по локатору {locator}")
            raise

    @allure.step('Возвращает текст элемента')
    def get_text(self, locator, time=10):
        element = self.find_element(locator, time)
        return element.text

    @allure.step('Прокручивает страницу к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Открывает новую вкладку и переходит по URL')
    def open_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}', '_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])