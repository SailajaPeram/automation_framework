from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium.webdriver.common.keys import Keys

def test_perform():
    # launching the browser
    driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    # selecting departure area
    depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((depart_from))).click()
    depart_from.send_keys("New Delhi")
    time.sleep(5)
    depart_from.send_keys(Keys.ENTER)
    # selecting destination area
    dest = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    time.sleep(5)
    dest.send_keys("New")
    time.sleep(10)
    suggestions = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
    print(len(suggestions))
    for result in suggestions:
        if "New York (JFK)" in result.text:
            result.click()
            time.sleep(5)
            break
    time.sleep(5)
    # selecting departure date
    suggestions = driver.find_elements(By.XPATH, '//div[@id="monthWrapper"]//tbody//td')
    print(len(suggestions))
    for result in suggestions:
        if result.get_attribute("data-date") == "31/10/2022":
            result.click()
            time.sleep(10)
            break
    # clicking on searchflight button
    button = driver.find_element(By.XPATH, '//*[@id="BE_flight_flsearch_btn"]')
    button.click()
    time.sleep(5)
    # closing the browser
    driver.close()



