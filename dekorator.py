import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def notifier(func):
    def wrapper(driver, *args, **kwargs):
        print("Test işləyir:", func.__name__)
        result = func(driver, *args, **kwargs)
        print("Test bitdi:", func.__name__)
        return result
    return wrapper

@pytest.fixture
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@notifier
def test_height(driver):
    eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
    assert eleCookiesDiv.value_of_css_property("height") == "155.2px", "Test 2 fail"

@notifier
def test_color(driver):
    eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
    assert eleCookiesDiv.value_of_css_property("background-color") == "rgba(255, 0, 0, 1)", "Test 2 fail"
