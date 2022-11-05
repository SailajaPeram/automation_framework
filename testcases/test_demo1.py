import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
@pytest.mark.usefixtures("setup")
class test_pythonframework():
    def test_perform(self):
        suggestions = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(suggestions))
        for result in suggestions:
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(6)
                break

        # clicking on origin button and date
        self.driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        time.sleep(5)
        Dates=self.driver.find_elements(By.XPATH,'//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')
        print(len(Dates))
        for date in Dates:
            if date.get_attribute("data-date")=="17/11/2022":
                date.click()
                time.sleep(5)
                break
        # clicking on flight search button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        search_flight_button=self.driver.find_element(By.XPATH,'//*[@id="BE_flight_flsearch_btn"]')
        search_flight_button.click()
        # driver.implicitly_wait(10)
        time.sleep(10)


