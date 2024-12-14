import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
