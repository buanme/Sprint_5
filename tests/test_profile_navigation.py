from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import URL_LOGIN_PAGE, LOGIN_NAME_INPUT_LOCATOR, LOGIN_PASSWORD_INPUT_LOCATOR, \
    LOGIN_SUBMIT_BUTTON_LOCATOR, LK_BUTTON_LOCATOR, URL_LK_PROFILE, CONSTRUCTOR_BUTTON_LOCATOR, URL_CONSTRUCTOR, \
    LOGO_LOCATOR


# Переход в личный кабинет по клику на «Личный кабинет».
def test_navigate_to_lk(driver, wait):
    driver.get(URL_LOGIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, LOGIN_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, LOGIN_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LK_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LK_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.url_to_be(URL_LK_PROFILE))
    assert driver.current_url == URL_LK_PROFILE
    driver.quit()


# Переход из личного кабинета в конструктор через клик на «Конструктор».
def test_navigate_from_lk_to_constructor(driver, wait):
    driver.get(URL_LOGIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, LOGIN_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, LOGIN_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LK_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LK_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, CONSTRUCTOR_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.url_to_be(URL_CONSTRUCTOR))
    assert driver.current_url == URL_CONSTRUCTOR
    driver.quit()


# Переход из личного кабинета в конструктор через клик на логотип Stellar Burgers.
def test_navigate_from_lk_to_constructor_with_logotip(driver, wait):
    driver.get(URL_LOGIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_NAME_INPUT_LOCATOR)))
    driver.find_element(By.XPATH, LOGIN_NAME_INPUT_LOCATOR).send_keys('Antonina_Bugaeva_13123@yandex.ru')
    driver.find_element(By.XPATH, LOGIN_PASSWORD_INPUT_LOCATOR).send_keys('123123123123')
    driver.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LK_BUTTON_LOCATOR)))
    driver.find_element(By.XPATH, LK_BUTTON_LOCATOR).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, LOGO_LOCATOR)))
    driver.find_element(By.XPATH, LOGO_LOCATOR).click()
    wait.until(expected_conditions.url_to_be(URL_CONSTRUCTOR))
    assert driver.current_url == URL_CONSTRUCTOR
    driver.quit()
