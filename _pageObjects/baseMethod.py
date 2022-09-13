from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Base(object):
    def __init__(self, driver):

        self._driver = driver

    def find_element(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located(
                element
            ))
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located(
                element
            ))
        except TimeoutException:
            return False
        #print(element_value)
        return element_value

    def verify_title(self, title):
        try:
            title_value = WebDriverWait(self, 15).until(EC.title_contains(
                title
            ))
        except TimeoutException:
            return False
        return title_value
