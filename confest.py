import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    # SETUP
    service = Service(executable_path=ChromeDriverManager().install())
    selenium_driver = webdriver.Chrome(service=service)
    yield selenium_driver
    # TEARDOWN
    time.sleep(5)
    selenium_driver.quit() #-
    