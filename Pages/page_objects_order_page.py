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
    def fill_first_page(self, first_name, last_name, address, phone_number, metro_station_locator):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.send_keys(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)

        metro_station_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_station_input.click()

        metro_station_item = self.wait_for_clickable(metro_station_locator)
        metro_station_item.click()
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняет вторую страницу формы заказа')
    def fill_second_page(self, delivery_date, rental_period_text, color, comment):
        delivery_date_input = self.find_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        delivery_date_input.send_keys(delivery_date)

        calendar_day = self.find_element(OrderPageLocators.CALENDAR_DAY)
        calendar_day.click()

        rental_period_dropdown = self.find_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_period_dropdown.click()

        rental_period_item_locator = (
            By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
        self.wait_and_click(rental_period_item_locator)

        if color == "black":
            self.click(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.SCOOTER_COLOR_GREY)

        comment_input = self.find_element(OrderPageLocators.COMMENT_INPUT)
        comment_input.send_keys(comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждает заказ')
    def confirm_order(self):
        confirmation_button = self.wait_for_clickable(OrderPageLocators.CONFIRMATION_BUTTON)

        self.driver.execute_script("arguments[0].click();", confirmation_button)

    @allure.step('Получает текст сообщения об успешном заказе')
    def get_order_success_message(self):
        return self.get_text(OrderPageLocators.ORDER_STATUS_BUTTON)