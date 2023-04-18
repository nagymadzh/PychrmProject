import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------------coursera-------------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.coursera.org/')
    return
    print("-----------------finished-----------------")
    driver.quit()

@pytest.mark.usefixtures('init_driver')
def test_google_title(init_driver):
    assert driver.title == "Coursera"

@pytest.mark.usefixtures('init_driver')
def test_google_url(init_driver):
    assert driver.url == "https://www.google.com/?safe=active&ssui=on"