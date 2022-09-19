# Campo de documento: //input[@id='document']
# Campo de senha:     //input[@id='password']
# Botão "Continuar":  //button[contains(text(), "Continuar")]

from selenium.webdriver.common.by import By


class LoginObjects(object):

    EDIT_DOCUMENT = (By.XPATH, "//input[@formcontrolname = 'document']")
    EDIT_PASSWORD = (By.XPATH, "//input[@formcontrolname = 'password']")
    BTN_LOGIN = (By.XPATH, "//button[contains(text(), 'Continuar')]")