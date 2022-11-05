import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    request.cls.driver=driver
    request.cls.wait=wait