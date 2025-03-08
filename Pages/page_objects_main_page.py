import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Кликает кнопку принятия куки, если она есть')
    def click_cookies_button(self):
        try:
            cookie_buttons = self.find_elements(MainPageLocators.COOKIES_BUTTON, time=3)

            if cookie_buttons:
                self.click(MainPageLocators.COOKIES_BUTTON)
                self.logger.info("Кнопка куки найдена и нажата")
            else:
                self.logger.info("Кнопка куки не найдена, продолжаем без нажатия")
        except Exception as e:
            self.logger.error(f"Не удалось кликнуть кнопку принятия куки: {e}")
        raise

    @allure.step('Кликает на вопрос в FAQ по номеру (1-8)')
    def click_faq_question(self, question_number):
        locator = (By.XPATH, f'//*[@id="accordion__heading-{question_number - 1}"]')

        self.scroll_to_element(locator)

        self.click(locator)

    @allure.step("Кликает на логотип Самоката")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликает на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step('Ожидает, пока URL страницы станет содержать "{url}" в течение {timeout} секунд')
    def wait_for_url_contains(self, url, timeout=10):
        self.wait_url_contains(url, timeout)

    @allure.step('Кликает на кнопку "Заказать" ({button_type})')
    def click_order_button(self, button_type):
        if button_type == "top":
            locator = MainPageLocators.ORDER_BUTTON_TOP
        elif button_type == "bottom":
            locator = MainPageLocators.ORDER_BUTTON_BOTTOM
        else:
            raise ValueError(f"Недопустимый тип кнопки: {button_type}. Допустимые значения: 'top', 'bottom'")
        self.click(locator)

    @allure.step('Получает текст ответа на вопрос FAQ по номеру {question_number}')
    def get_faq_answer_text(self, question_number):
        locator = (By.XPATH, f'//*[@id="accordion__panel-{question_number - 1}"]/p')
        return self.get_text(locator)