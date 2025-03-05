import allure
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from locators import OrderPageLocators
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging

class OrderPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step('Заполняет первую страницу формы заказа')
    def fill_first_page(self, first_name, last_name, address, phone_number, metro_station_text):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

        metro_station_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_station_input.click()

        metro_station_locator = OrderPageLocators.metro_station_item_locator(metro_station_text)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(metro_station_locator))
        metro_station_item = self.driver.find_element(*metro_station_locator)
        metro_station_item.click()
        print("Кликаем по кнопке Далее")
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Заполняет вторую страницу формы заказа, выбирая срок аренды')
    def fill_second_page(self, delivery_date, rental_period_text, color, comment):

        delivery_date_input = self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_INPUT)
        delivery_date_input.send_keys(delivery_date)

        calendar_day = self.driver.find_element(By.XPATH,
                                                "//div[contains(@class, 'react-datepicker__day') and text()='1']")  # Кликаем на 1-е число
        calendar_day.click()

        rental_period_dropdown = self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
            )

            rental_period_dropdown.click()

        except TimeoutException:
            raise

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded='true']"))
            )
        except TimeoutException:
            raise

        rental_period_item_locator = (
            By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
        try:
            rental_period_item = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(rental_period_item_locator)
            )
            self.driver.execute_script("arguments[0].click();", rental_period_item)
        except TimeoutException:
            raise

        if color == "black":
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY).click()

        comment_input = self.driver.find_element(*OrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(comment)
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Подтверждает заказ')
    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRMATION_BUTTON)
        )
        self.driver.find_element(*OrderPageLocators.CONFIRMATION_BUTTON).click()

    @allure.step('Получает текст сообщения об успешном заказе')
    def get_order_success_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.ORDER_STATUS_BUTTON)
        )
        return self.driver.find_element(*OrderPageLocators.ORDER_STATUS_BUTTON).text
