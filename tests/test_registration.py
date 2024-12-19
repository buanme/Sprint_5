import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import Locators
from tests.urls import Urls


class TestRegistrationScenarios:
    # Успешная регистрация
    def test_successful_registration_with_valid_data(self, driver, wait):
        email = f'Antonina_Bugaeva_13{random.randint(100000, 1000000)}@yandex.ru'
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.REGISTRATION_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.REGISTRATION_NAME_INPUT).send_keys('Antonina Bugaeva')
        driver.find_element(By.XPATH, Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.REGISTRATION_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE

    # Ошибка для некорректного пароля
    def test_error_for_invalid_password(self, driver, wait):
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.REGISTRATION_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.REGISTRATION_NAME_INPUT).send_keys('Antonina Bugaeva')
        driver.find_element(By.XPATH, Locators.REGISTRATION_EMAIL_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.REGISTRATION_PASSWORD_INPUT).send_keys('12345')
        driver.find_element(By.XPATH, Locators.REGISTRATION_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.INVALID_PASSWORD_ERROR)))
        assert driver.find_element(By.XPATH, Locators.INVALID_PASSWORD_ERROR) is not None
