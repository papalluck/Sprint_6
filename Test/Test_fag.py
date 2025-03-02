import pytest
import allure
from selenium import webdriver
from Pages.page_objects_main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import Urls
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



@allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
class TestFAQ:
    @allure.step('Открываем браузер Firefox')
    def setup_method(self, method):
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service)
        self.driver.get(Urls.BASE_URL)
        self.main_page = MainPage(self.driver)

    @allure.step('Закрываем браузер')
    def teardown_method(self, method):
        self.driver.quit()

    @allure.description('Проверяем,что при клике на вопрос открывается соответствующий текст')
    @pytest.mark.parametrize("question_number", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_faq_answers_are_displayed(self, question_number):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//*[@id="accordion__heading-{question_number - 1}"]'))
            )
        except Exception as e:
            print(f"Не удалось дождаться загрузки вопроса {question_number}: {e}")
            raise

        self.main_page.click_faq_question(question_number)

        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f'//div[@id="accordion__panel-{question_number - 1}"]/p'))
            )
        except Exception as e:
            print(f"Не удалось дождаться загрузки ответа на вопрос {question_number}: {e}")
            raise

        actual_answer_text = self.main_page.get_faq_answer_text(question_number)

        if question_number == 1:
            expected_answer_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        elif question_number == 2:
            expected_answer_text = "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        elif question_number == 3:
            expected_answer_text = "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
        elif question_number == 4:
            expected_answer_text = "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        elif question_number == 5:
            expected_answer_text = "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        elif question_number == 6:
            expected_answer_text = "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        elif question_number == 7:
            expected_answer_text = "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        elif question_number == 8:
            expected_answer_text = "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        else:
            raise ValueError("Invalid question number. Must be between 1 and 8.")


        assert actual_answer_text == expected_answer_text, f"Для вопроса {question_number} ожидался ответ '{expected_answer_text}', но получен '{actual_answer_text}'"