import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Кликает кнопку принятия куки')
    def click_cookies_button(self):
        self.click(MainPageLocators.COOKIES_BUTTON)

    @allure.step('Кликает на вопрос в FAQ по номеру (1-8)')
    def click_faq_question(self, question_number):
        locator = (By.XPATH, f'//*[@id="accordion__heading-{question_number - 1}"]')
        self.click(locator)

    @allure.step('Возвращает текст ответа в FAQ по номеру (1-8)')
    def get_faq_answer_text(self, question_number):
        locator = (By.XPATH, f'//div[@id="accordion__panel-{question_number - 1}"]/p')
        return self.get_text(locator)

    @allure.step('Кликает кнопку заказа (вверху или внизу страницы)')
    def click_order_button(self, button_type):
        if button_type == "top":
            locator = MainPageLocators.ORDER_BUTTON_TOP
        else:
            locator = MainPageLocators.ORDER_BUTTON_BOTTOM

        try:
            element = self.find_element(locator)

            if button_type == "bottom":
                self.scroll_to_element(element)

            self.click(locator)

        except TimeoutException:
            self.logger.exception(f"Не удалось найти или кликнуть кнопку 'Заказать' ({button_type})")
            self.logger.debug(f"Текущий HTML:\n{self.driver.page_source}")
            raise

    @allure.step('Кликает на логотип «Самоката»')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликает на логотип Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

