# Botão para verificar se o Cliente já está cadastrado: //button[@class = 'mat-tooltip-trigger btn btn-search-customer']

# Campos datepicker: //ejs-datepicker[@formcontrolname='cnhDateExpiration']//input
# ID's: dateBirth, cnhDateFirst e cnhDateExpiration

# Campos text:       //input[@formcontrolname = 'cpfCnpj']
# ID's: cpfCnpj, name, nameMother, rg, rgIssuer, cnh, cnhNumber (Número de segurança),
# dddPhone, phone, dddOne, phoneOne, email, addressZipCode, addressNumber

# Campos dropdown:    //ejs-dropdownlist[@formcontrolname='{locator}']
# ID's: gender, codCareer, cnhIsoCountry, cnhState, addressCoutry

import json
from time import sleep
import pyautogui as PG
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
#driver.get("https://easy.unidas.com.br/login")
driver.get("https://easy.hml.unidas.com.br/login")
wait = WebDriverWait(driver, 10)

# Função para aguardar a tela de carregamento
def loadScreenWait():
    element = wait.until(EC.visibility_of_element_located((
        By.XPATH, "//div[@class='overlay ng-tns-c49-0 ng-trigger ng-trigger-fadeIn ng-star-inserted ng-animating']")))

    sleep(15)

    """wait.until(EC.invisibility_of_element_located((
        By.XPATH, "//div[@class='overlay ng-tns-c49-0 ng-trigger ng-trigger-fadeIn ng-star-inserted ng-animating']")))"""

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
def comboInteract(locator, value):
    element = wait.until(EC.presence_of_element_located((
        By.XPATH, f"//ejs-dropdownlist[@formcontrolname = '{locator}']")))
    ActionChains(driver)\
        .move_to_element(element)\
        .click()\
        .perform()

    element_value = wait.until(EC.presence_of_element_located((
        By.XPATH, f"//li[contains(text(), '{value}')]")))
    ActionChains(driver)\
        .pause(0.5)\
        .move_to_element(element_value)\
        .click()\
        .perform()

def documents_sending():
    pass

# Função para percorrer o arquivo jSon e chamar as funções
# de preenchimento de acordo com o tipo do campo. CPF 913.466.068-20
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
                        # Remover para realizar o fluxo completo de cadastro de cliente @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                        #//button[@class = 'mat-tooltip-trigger btn btn-search-customer']
                        wait.until(EC.element_to_be_clickable((
                            By.XPATH, "//button[@class = 'mat-tooltip-trigger btn btn-search-customer']"))).click()
                        user_exist = wait.until(EC.text_to_be_present_in_element_value((
                            By.XPATH, "//input[@formcontrolname = 'name']"), "LEONARDO HERNANDEZ"))
                        if user_exist:
                            PG.alert(text='Usuário existe!', title='Sucesso!', button='OK')
                            #avançar para a tela de documentos
                            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'submit']"))).click()
                            wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text() = 'Usuário atualizado com sucesso.']")))
                            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'OK')]"))).click()
                            titulo = wait.until(EC.visibility_of_element_located((By.XPATH, "//h5[text() = 'Importação de Arquivos']")))
                            if titulo:
                                PG.alert(text='Tela de importação de arquivos!', title='Sucesso!', button='OK')
                                #Informar documentos
                                select_element = wait.until(EC.visibility_of_element_located((
                                    By.XPATH, "//select[@class = 'form-control']")))
                                select_element = Select(select_element)
                                select_element.select_by_visible_text("Foto do Rosto")
                            return False
                        # Remover para realizar o fluxo completo de cadastro de cliente @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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
        documents_sending()
        print('='*15 + f'Fim {client}' + '='*15)


wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'document']"))).send_keys("46435591873")

wait.until(EC.visibility_of_element_located((
    By.XPATH, "//input[@formcontrolname = 'password']"))).send_keys("teste123") 

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
