import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import ElementClickInterceptedException as ECIexception, TimeoutException


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://easy.unidas.com.br/login")
wait = WebDriverWait(driver, 15)

sleep(3)
edit_login = driver.find_element(By.XPATH, "//input[@formcontrolname = 'document']").send_keys("41328599833")
sleep(1)
edit_password = driver.find_element(By.XPATH, "//input[@formcontrolname = 'password']").send_keys("a@449f9054")
sleep(1)
btn_login = driver.find_element(By.XPATH, "//button[contains(text(), 'Continuar')]").click()
sleep(4)

sleep(1)
btn_menu = driver.find_element(By.XPATH, "//und-menu-outlined-icon[@class = 'text-white menu-icon']").click()
sleep(2)
menu_item_records = driver.find_element(By.XPATH, "//li[2]/div").click()
sleep(2)
subitem_br_customer = driver.find_element(By.XPATH, "//li[2]/ul/li/div").click()
sleep(1)

def file_reading(filedir):
    with open(filedir, 'r') as file:
        person = json.loads(file.read())
    return person

def is_dropdown(element):
    try:
        element = wait.until(EC.element_attribute_to_include((
            By.XPATH, f"//input[@formcontrolname = '{element}']"), 
            "aria-expanded"))
    except TimeoutException:
        print('Erro ao carregar elemento: TimeoutException.')
        return False
    return element

def registration_filling():
    person = file_reading(filedir="./person.json")
    for k_data, v_data in person.items():
        print(k_data, v_data)
        #//input[@formcontrolname = 'cpfCnpj']
        try:
            element = wait.until(EC.visibility_of_element_located((
                By.XPATH, f"//input[@formcontrolname = '{k_data}']")))
            
            element = wait.until(EC.presence_of_element_located((
                By.XPATH, f"//input[@formcontrolname = '{k_data}']")))
            
            if is_dropdown(k_data):
                return True
        except ECIexception:
            print('Erro ao clicar no elemento: ECIexception.')
            return False
        except TimeoutException:
            print('Erro ao aguardar pelo elemento: TimeoutException.')
            return False
        return element

registration_filling()