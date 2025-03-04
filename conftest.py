import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import logging

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver():
    logger.info("Начинаем настройку драйвера")
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("Драйвер закрыт")