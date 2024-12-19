from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from locators import Locators
from urls import Urls


class TestNavigationScenarios:
    # Переход в личный кабинет по клику на «Личный кабинет».
    def test_navigate_to_lk(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.LOGIN_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.LOGIN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LK_BUTTON)))
        driver.find_element(By.XPATH, Locators.LK_BUTTON).click()
        wait.until(expected_conditions.url_to_be(Urls.LK_PROFILE_PAGE))
        assert driver.current_url == Urls.LK_PROFILE_PAGE

    # Переход из личного кабинета в конструктор через клик на «Конструктор».
    def test_navigate_from_lk_to_constructor(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.LOGIN_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.LOGIN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LK_BUTTON)))
        driver.find_element(By.XPATH, Locators.LK_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.CONSTRUCTOR_BUTTON)))
        driver.find_element(By.XPATH, Locators.CONSTRUCTOR_BUTTON).click()
        wait.until(expected_conditions.url_to_be(Urls.CONSTRUCTOR_PAGE))
        assert driver.current_url == Urls.CONSTRUCTOR_PAGE

    # Переход из личного кабинета в конструктор через клик на логотип Stellar Burgers.
    def test_navigate_from_lk_to_constructor_with_logotip(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.LOGIN_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.LOGIN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LK_BUTTON)))
        driver.find_element(By.XPATH, Locators.LK_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGO)))
        driver.find_element(By.XPATH, Locators.LOGO).click()
        wait.until(expected_conditions.url_to_be(Urls.CONSTRUCTOR_PAGE))
        assert driver.current_url == Urls.CONSTRUCTOR_PAGE
