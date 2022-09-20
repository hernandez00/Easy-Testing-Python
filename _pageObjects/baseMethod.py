from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException as ECIException


class Base(object):
    def __init__(self, driver):

        self._driver = driver
        #15 = 15
        #self._wait = WebDriverWait(driver, timeout)

    # Metodo para verificar se um elemento está presente e visível
    def find_element(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located(
                element
            ))
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located(
                element
            ))
        except ECIException:
            element_value = WebDriverWait(self, 15).until(EC.element_to_be_clickable(
                element
            ))
        except TimeoutException:
            return False
        #print(element_value)
        return element_value

    # Metodo para verificar se o campo é um ComboBox
    def is_dropdown(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.element_attribute_to_include(
                element, "aria-expanded"
            ))
        except TimeoutException:
            return False
        return element_value

    # Metodo para verificar o título da página
    def verify_title(self, title):
        try:
            title_value = WebDriverWait(self, 15).until(EC.title_contains(
                title
            ))
        except TimeoutException:
            return False
        return title_value
    
    #//h2[text() = 'CADASTRO DO CLIENTE NACIONAL']
    def find_component_title(self, element):
        try:
            element_value = WebDriverWait(self, 15).until(EC.presence_of_element_located(
                element
            ))
            element_value = WebDriverWait(self, 15).until(EC.visibility_of_element_located(
                element
            ))
            sleep(3)
        except TimeoutException:
            return False
        print(element_value)
        return element_value