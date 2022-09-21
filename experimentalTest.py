# Botão para verificar se o Cliente já está cadastrado: //button[@class = 'mat-tooltip-trigger btn btn-search-customer']

# Campos datepicker: //ejs-datepicker[@formcontrolname='cnhDateExpiration']//input
# ID's: dateBirth, cnhDateFirst e cnhDateExpiration

# Campos text:       //input[@formcontrolname = 'cpfCnpj']
# ID's: cpfCnpj, name, nameMother, rg, rgIssuer, cnh, cnhNumber (Número de segurança),
# dddPhone, phone, dddOne, phoneOne, email, addressZipCode, addressNumber

# Campos dropdown:    //ejs-dropdownlist[@formcontrolname='gender']
# ID's: gender, codCareer, cnhIsoCountry, cnhState, addressCoutry

import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import ElementClickInterceptedException as ECIexception, TimeoutException


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.set_window_size(1600, 900)
driver.get("https://easy.unidas.com.br/login")
#driver.get("https://easy.hml.unidas.com.br/login")
wait = WebDriverWait(driver, 10)


def file_reading(filedir):
    with open(filedir, 'r') as file:
        person = json.loads(file.read())
    return person


def registration_filling(filedir="./person.json"):
    person = file_reading(filedir)
    for k_data, v_data in person.items():
            print(k_data)
            for k, v in v_data.items():
                if k_data == "text":
                    locator = f"//input[@formcontrolname = '{k}']"
                elif k_data == "datePicker":
                    locator = f"//ejs-datepicker[@formcontrolname='{k}']//input"
                else:
                    locator = f"//ejs-dropdownlist[@formcontrolname='{k}']"
                try:
                    element = wait.until(EC.visibility_of_element_located((
                        By.XPATH, locator)))

                    element = wait.until(EC.presence_of_element_located((
                        By.XPATH, locator)))
                except ECIexception:
                    print(f'Erro ao clicar no elemento {k}: ECIexception.')
                    return False
                except TimeoutException:
                    print(
                        f'Erro ao aguardar pelo elemento {k}: TimeoutException.')
                    return False
                element.send_keys(v)


wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'document']"))).send_keys("41328599833")  # 41328599833

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'password']"))).send_keys("a@449f9054")    # a@449f9054

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//button[contains(text(), 'Continuar')]"))).click()

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//und-menu-outlined-icon[@class = 'text-white menu-icon']"))).click()

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//li[2]/div"))).click()

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//li[2]/ul/li/div"))).click()

registration_filling()
