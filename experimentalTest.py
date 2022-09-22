# Botão para verificar se o Cliente já está cadastrado: //button[@class = 'mat-tooltip-trigger btn btn-search-customer']

# Campos datepicker: //ejs-datepicker[@formcontrolname='cnhDateExpiration']//input
# ID's: dateBirth, cnhDateFirst e cnhDateExpiration

# Campos text:       //input[@formcontrolname = 'cpfCnpj']
# ID's: cpfCnpj, name, nameMother, rg, rgIssuer, cnh, cnhNumber (Número de segurança),
# dddPhone, phone, dddOne, phoneOne, email, addressZipCode, addressNumber

# Campos dropdown:    //ejs-dropdownlist[@formcontrolname='{locator}']
# ID's: gender, codCareer, cnhIsoCountry, cnhState, addressCoutry

import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import ElementClickInterceptedException as ECIexception, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.set_window_size(1600, 900)
# driver.get("https://easy.unidas.com.br/login")
driver.get("https://easy.hml.unidas.com.br/login")
wait = WebDriverWait(driver, 10)

# Função para aguardar a tela de carregamento
""" @@@@@@@@@@@@@@@@@@@@ Ainda não está 100% funcional @@@@@@@@@@@@@@@@@@@@ """
def loadScreenWait():
    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[@class='overlay ng-tns-c49-0 ng-trigger ng-trigger-fadeIn ng-star-inserted']"
    )))

    wait.until(EC.invisibility_of_element_located((
        By.XPATH, "//div[@class='overlay ng-tns-c49-0 ng-trigger ng-trigger-fadeIn ng-star-inserted']"
    )))

# Função para ler o arquivo jSon
def file_reading(filedir):
    with open(filedir, 'r') as file:
        person = json.loads(file.read())
    return person

# Função para preencher campos do tipo Text
def textInteract(locator, value):
    element = wait.until(EC.visibility_of_element_located((
        By.XPATH, f"//input[@formcontrolname = '{locator}']")))

    element.send_keys(value)

    if locator == 'addressZipCode':
        element.send_keys(Keys.TAB)
        loadScreenWait()

# Função para preencher campos do tipo Date Picker
def datePickerInteract(locator, value):
    element = wait.until(EC.visibility_of_element_located((
        By.XPATH, f"//ejs-datepicker[@formcontrolname='{locator}']//input")))

    ActionChains(driver)\
        .move_to_element(element)\
        .double_click()\
        .click_and_hold()\
        .send_keys_to_element(element, value)\
        .perform()

# Função para preencher campos do tipo ComboBox
""" @@@@@@@@@@@@@@@@@@@@ Ainda não está 100% funcional @@@@@@@@@@@@@@@@@@@@ """
def comboInteract(locator, value):
    element = wait.until(EC.presence_of_element_located((
        By.XPATH, f"//ejs-dropdownlist[@formcontrolname = '{locator}']"))).click()

    element_value = wait.until(EC.presence_of_element_located((
        By.XPATH, f"//li[contains(text(), '{value}')]"))).click()

# Função para percorrer o arquivo jSon e chamar as funções
# de preenchimento de acordo com o tipo do campo.
def registration_filling(filedir="./person.json"):
    person = file_reading(filedir)
    for client, data in person.items():
        print(client)
        for k_data, v_data in data.items():
            print(k_data)
            for k, v in v_data.items():
                print(f"{k}, {v}")
                try:
                    if k_data == "text":
                        textInteract(k, v)
                    elif k_data == "datePicker":
                        datePickerInteract(k, v)
                    else:
                        comboInteract(k, v)
                except ECIexception:
                    print(f'Erro ao clicar no elemento {k}: ECIexception.')
                    return False
                except TimeoutException:
                    print(
                        f'Erro ao aguardar pelo elemento {k}: TimeoutException.')
                    return False
        print('='*15 + f'Fim {client}' + '='*15)


wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'document']"))).send_keys("46435591873")  # 41328599833

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'password']"))).send_keys("teste123")     # a@449f9054

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//button[contains(text(), 'Continuar')]"))).click()

loadScreenWait()

wait.until(EC.element_to_be_clickable((
    By.XPATH, "//und-menu-outlined-icon[@class = 'text-white menu-icon']"))).click()

wait.until(EC.element_to_be_clickable((
    By.XPATH, "//li[2]/div"))).click()

wait.until(EC.element_to_be_clickable((
    By.XPATH, "//li[2]/ul/li/div"))).click()

registration_filling()
