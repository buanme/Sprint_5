from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from locators import Locators
from urls import Urls


class TestLoginScenarios:
    def test_login_button_entrance_main_page(self, driver, wait):
        driver.get(Urls.MAIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locators.LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.AUTH_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.AUTH_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.AUTH_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.AUTH_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ORDER_BUTTON)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTTON)) == 1

    def test_login_lk_button(self, driver, wait):
        driver.get(Urls.MAIN_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, Locators.ACCOUNT_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.AUTH_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.AUTH_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.AUTH_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.AUTH_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ORDER_BUTTON)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTTON)) == 1

    def test_login_button_registration(self, driver, wait):
        driver.get(Urls.REGISTER_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locators.REGISTRATION_LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.AUTH_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.AUTH_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.AUTH_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.AUTH_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ORDER_BUTTON)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTTON)) == 1

    def test_login_button_forgot_password(self, driver, wait):
        driver.get(Urls.FORGOT_PASSWORD_PAGE)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.FORGOT_PASSWORD_LOGIN_BUTTON)))
        driver.find_element(By.XPATH, Locators.FORGOT_PASSWORD_LOGIN_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, Locators.AUTH_NAME_INPUT)))
        driver.find_element(By.XPATH, Locators.AUTH_NAME_INPUT).send_keys('Antonina_Bugaeva_13123@yandex.ru')
        driver.find_element(By.XPATH, Locators.AUTH_PASSWORD_INPUT).send_keys('123123123123')
        driver.find_element(By.XPATH, Locators.AUTH_SUBMIT_BUTTON).click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, Locators.ORDER_BUTTON)))
        assert len(driver.find_elements(By.XPATH, Locators.ORDER_BUTTON)) == 1
    