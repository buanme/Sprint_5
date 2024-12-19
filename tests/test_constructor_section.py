from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.locators import Locators
from tests.urls import Urls


class TestTabNavigationScenarios:
    # Переход к разделу 'Булки'
    def test_bun_tab(self, driver, wait):
        driver.get(Urls.MAIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.BULKY_TAB)))
        driver.find_element(By.XPATH, Locators.SAUCE_TAB).click()
        driver.find_element(By.XPATH, Locators.BULKY_TAB).click()
        assert Locators.ACTIVE_CLASS in driver.find_element(By.XPATH, Locators.BULKY_TAB).get_attribute("class")

    # Переход к разделу 'Соусы'
    def test_sauce_tab(self, driver, wait):
        driver.get(Urls.MAIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.SAUCE_TAB)))
        driver.find_element(By.XPATH, Locators.SAUCE_TAB).click()
        assert Locators.ACTIVE_CLASS in driver.find_element(By.XPATH, Locators.SAUCE_TAB).get_attribute("class")

    # Переход к разделу 'Начинки'
    def test_main_tab(self, driver, wait):
        driver.get(Urls.MAIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.NACHINKY_TAB)))
        driver.find_element(By.XPATH, Locators.NACHINKY_TAB).click()
        assert Locators.ACTIVE_CLASS in driver.find_element(By.XPATH, Locators.NACHINKY_TAB).get_attribute("class")
