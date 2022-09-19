# Título <h2> da página:    //h2[text() = 'CADASTRO DO CLIENTE NACIONAL']

# Campo cpfCnpj:            //input[@formcontrolname = 'cpfCnpj']
# Campo name:               //input[@formcontrolname = 'name']


from selenium.webdriver.common.by import By


class CustomerRegistrationObjects(object):
    
    COMPONENT_TITLE = (By.XPATH, "//h2[text() = 'CADASTRO DO CLIENTE NACIONAL']")