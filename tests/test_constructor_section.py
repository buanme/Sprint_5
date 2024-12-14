from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import URL_MAIN_PAGE, BULKY_TAB_LOCATOR, SAUCE_TAB_LOCATOR, ACTIVE_CLASS, NACHINKY_TAB_LOCATOR


# Переход к разделу 'Булки'
def test_bun_tab(driver, wait):
    driver.get(URL_MAIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, BULKY_TAB_LOCATOR)))
    driver.find_element(By.XPATH, SAUCE_TAB_LOCATOR).click()
    driver.find_element(By.XPATH, BULKY_TAB_LOCATOR).click()
    assert ACTIVE_CLASS in driver.find_element(By.XPATH, BULKY_TAB_LOCATOR).get_attribute("class")
    driver.quit()


# Переход к разделу 'Соусы'
def test_sauce_tab(driver, wait):
    driver.get(URL_MAIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, SAUCE_TAB_LOCATOR)))
    driver.find_element(By.XPATH, SAUCE_TAB_LOCATOR).click()
    assert ACTIVE_CLASS in driver.find_element(By.XPATH, SAUCE_TAB_LOCATOR).get_attribute("class")
    driver.quit()


# Переход к разделу 'Начинки'
def test_main_tab(driver, wait):
    driver.get(URL_MAIN_PAGE)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH, NACHINKY_TAB_LOCATOR)))
    driver.find_element(By.XPATH, NACHINKY_TAB_LOCATOR).click()
    assert ACTIVE_CLASS in driver.find_element(By.XPATH, NACHINKY_TAB_LOCATOR).get_attribute("class")
    driver.quit()
