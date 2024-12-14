from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import URL_MAIN_PAGE, LOGIN_BUTTON_LOCATOR, AUTH_NAME_INPUT_LOCATOR, AUTH_PASSWORD_INPUT_LOCATOR, \
    AUTH_SUBMIT_BUTTON_LOCATOR, ORDER_BUTTON_LOCATOR, ACCOUNT_BUTTON_LOCATOR, REGISTRATION_LOGIN_BUTTON_LOCATOR, \
    FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR


def test_login_button_entrance_main_page(driver, wait):
    driver.get(URL_MAIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LOGIN_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, AUTH_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, AUTH_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, AUTH_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, AUTH_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ORDER_BUTTON_LOCATOR)))
    assert len(driver.find_elements(By.XPATH, ORDER_BUTTON_LOCATOR)) == 1
    driver.quit()


def test_login_lk_button(driver, wait):
    driver.get(URL_MAIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ACCOUNT_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, ACCOUNT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, AUTH_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, AUTH_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, AUTH_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, AUTH_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ORDER_BUTTON_LOCATOR)))
    assert len(driver.find_elements(By.XPATH, ORDER_BUTTON_LOCATOR)) == 1
    driver.quit()


def test_login_button_registration(driver, wait):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, REGISTRATION_LOGIN_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, REGISTRATION_LOGIN_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, AUTH_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, AUTH_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, AUTH_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, AUTH_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ORDER_BUTTON_LOCATOR)))
    assert len(driver.find_elements(By.XPATH, ORDER_BUTTON_LOCATOR)) == 1
    driver.quit()


def test_login_button_forgot_password(driver, wait):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, FORGOT_PASSWORD_LOGIN_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, AUTH_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, AUTH_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, AUTH_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, AUTH_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, ORDER_BUTTON_LOCATOR)))
    assert len(driver.find_elements(By.XPATH, ORDER_BUTTON_LOCATOR)) == 1
    driver.quit()
