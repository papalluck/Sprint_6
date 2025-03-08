import pytest
import allure
from Pages.page_objects_main_page import MainPage
from urls import Urls
import logging
import time

logger = logging.getLogger(__name__)

@allure.title('Проверка раздела «Вопросы о важном»')
class TestFAQ:

    @pytest.fixture(scope="function")
    def setup(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.driver.get(Urls.BASE_URL)
        return self.main_page

    @pytest.mark.parametrize(
        "question_number, expected_answer",
        [
            (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
            (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
            (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
            (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
            (6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
            (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
            (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
        ],
    )
    @pytest.mark.order(2)
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    def test_faq_answer(self, setup, question_number, expected_answer):
        logger.info(f"Проверяем вопрос {question_number} с ответом: {expected_answer}")
        main_page = setup

        main_page.click_faq_question(question_number)
        time.sleep(0.5)
        actual_answer = main_page.get_faq_answer_text(question_number)

        assert actual_answer == expected_answer, f"Ожидаемый ответ: {expected_answer}, Фактический ответ: {actual_answer}"

