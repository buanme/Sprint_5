import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import URL_REGISTER_PAGE, REGISTRATION_NAME_INPUT_LOCATOR, REGISTRATION_EMAIL_INPUT_LOCATOR, \
    REGISTRATION_PASSWORD_INPUT_LOCATOR, REGISTRATION_SUBMIT_BUTTON_LOCATOR, INVALID_PASSWORD_ERROR_LOCATOR


# Успешная регистрация
def test_successful_registration_with_valid_data(driver, wait):
    email = f'Antonina_Bugaeva_13{random.randint(100000, 1000000)}@yandex.ru'
    driver.get(URL_REGISTER_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, REGISTRATION_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, REGISTRATION_NAME_INPUT_LOCATOR).send_keys('Antonina Bugaeva')
    driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT_LOCATOR).send_keys(email)
    driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, REGISTRATION_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()


# Ошибка для некорректного пароля
def test_error_for_invalid_password(driver, wait):
    driver.get(URL_REGISTER_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, REGISTRATION_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, REGISTRATION_NAME_INPUT_LOCATOR).send_keys('Antonina Bugaeva')
    driver.find_element(By.XPATH, REGISTRATION_EMAIL_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, REGISTRATION_PASSWORD_INPUT_LOCATOR).send_keys('12345')
    driver.find_element(By.XPATH, REGISTRATION_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, INVALID_PASSWORD_ERROR_LOCATOR)))
    assert driver.find_element(By.XPATH, INVALID_PASSWORD_ERROR_LOCATOR) is not None
    driver.quit()
