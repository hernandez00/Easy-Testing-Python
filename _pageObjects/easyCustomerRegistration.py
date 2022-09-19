from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pageObjects.baseMethod import Base
from _pageObjects._locators.customerRegistration import CustomerRegistrationObjects as CRO


class EasyCustomerRegistration(Base):

    def is_br_registration(self):
        is_br_reg = Base.find_component_title(self._driver, CRO.COMPONENT_TITLE)
        if is_br_reg:
            print("Cadastro de cliente Brasileiro acessado com sucesso!")
        else:
            print("Falha ao acessar cadastro de cliente brasileiro.")
        return is_br_reg