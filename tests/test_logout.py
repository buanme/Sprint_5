from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import URL_LOGIN_PAGE, LOGIN_NAME_INPUT_LOCATOR, LOGIN_PASSWORD_INPUT_LOCATOR, \
    LOGIN_SUBMIT_BUTTON_LOCATOR, LK_BUTTON_LOCATOR, LOGOUT_BUTTON_LOCATOR, URL_AFTER_LOGOUT


# Выход из аккаунта по кнопке «Выйти» в личном кабинете.
def test_logout_from_lk(driver, wait):
    driver.get(URL_LOGIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, LOGIN_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, LOGIN_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LK_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LK_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGOUT_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LOGOUT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.url_to_be(URL_AFTER_LOGOUT))
    assert driver.current_url == URL_AFTER_LOGOUT
    driver.quit()
