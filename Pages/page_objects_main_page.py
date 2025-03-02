import time
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
import pytest
import allure



class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_cookies_button(self):
        """Кликает кнопку принятия куки."""
        self.driver.find_element(*MainPageLocators.COOKIES_BUTTON).click()

    def click_faq_question(self, question_number):
        """Кликает на вопрос в FAQ по номеру (1-8)."""
        if question_number == 1:
            locator = MainPageLocators.FAQ_QUESTIONS_1
        elif question_number == 2:
            locator = MainPageLocators.FAQ_QUESTIONS_2
        elif question_number == 3:
            locator = MainPageLocators.FAQ_QUESTIONS_3
        elif question_number == 4:
            locator = MainPageLocators.FAQ_QUESTIONS_4
        elif question_number == 5:
            locator = MainPageLocators.FAQ_QUESTIONS_5
        elif question_number == 6:
            locator = MainPageLocators.FAQ_QUESTIONS_6
        elif question_number == 7:
            locator = MainPageLocators.FAQ_QUESTIONS_7
        elif question_number == 8:
            locator = MainPageLocators.FAQ_QUESTIONS_8
        else:
            raise ValueError("Invalid question number. Must be between 1 and 8.")

        element = self.driver.find_element(*locator)
        element.click()
        return self

    def get_faq_answer_text(self, question_number):
        """Возвращает текст ответа в FAQ по номеру (1-8)."""
        if question_number == 1:
            locator = MainPageLocators.FAQ_ANSWER_1
        elif question_number == 2:
            locator = MainPageLocators.FAQ_ANSWER_2
        elif question_number == 3:
            locator = MainPageLocators.FAQ_ANSWER_3
        elif question_number == 4:
            locator = MainPageLocators.FAQ_ANSWER_4
        elif question_number == 5:
            locator = MainPageLocators.FAQ_ANSWER_5
        elif question_number == 6:
            locator = MainPageLocators.FAQ_ANSWER_6
        elif question_number == 7:
            locator = MainPageLocators.FAQ_ANSWER_7
        elif question_number == 8:
            locator = MainPageLocators.FAQ_ANSWER_8
        else:
            raise ValueError("Invalid question number. Must be between 1 and 8.")

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)
        return element.text

    def click_order_button(self, button_type):
        """Кликает кнопку заказа (вверху или внизу страницы)."""
        if button_type == "top":
            locator = MainPageLocators.ORDER_BUTTON_TOP
        else:
            locator = MainPageLocators.ORDER_BUTTON_BOTTOM

        try:
            # Явно ждем, пока элемент не появится на странице и станет видимым
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )

            # Прокручиваем страницу до элемента (только для нижней кнопки)
            if button_type == "bottom":
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(2)  # Даем больше времени на прокрутку

            # Явно ждем, пока элемент не станет кликабельным
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )

            element.click()  # Используем элемент, найденный локатором
        except TimeoutException:
            print(f"Не удалось найти или кликнуть кнопку 'Заказать' ({button_type})")
            print("Текущий HTML:")
            print(self.driver.page_source)
            raise

    def click_scooter_logo(self):
        """Кликает на логотип «Самоката»."""
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        """Кликает на логотип Яндекса."""
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()

