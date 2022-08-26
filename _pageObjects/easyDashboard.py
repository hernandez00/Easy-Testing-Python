from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pageObjects._locators.dashboardLocators import DashboardObjects
from _pageObjects.baseMethod import Base


class EasyDashboard(Base):

    def openCotation(self):
        btn_cotation = Base.find_element(
            self._driver, DashboardObjects.btn_cotation)
        btn_cotation.click()

    def is_cotation(self):
        is_cotation = Base.verify_title(self._driver, "Contrato") #Deveria ser "Cotação"
        if is_cotation:
            print('Fluxo de cotação iniciado com sucesso!')
        else:
            print('Falha ao iniciar fluxo de cotação!')