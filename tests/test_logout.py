from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from locators import Locators
from urls import Urls


class TestLogoutScenario:
    # Выход из аккаунта по кнопке «Выйти» в личном кабинете.
    def test_logout_from_lk(self, driver, wait):
        driver.get(Urls.LOGIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.LOGIN_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.LOGIN_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.LOGIN_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LK_BUTTON)))
        driver.find_element(By.XPATH, Locators.LK_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGOUT_BUTTON)))
        driver.find_element(By.XPATH, Locators.LOGOUT_BUTTON).click()
        wait.until(expected_conditions.url_to_be(Urls.AFTER_LOGOUT_PAGE))
        assert driver.current_url == Urls.AFTER_LOGOUT_PAGE
    