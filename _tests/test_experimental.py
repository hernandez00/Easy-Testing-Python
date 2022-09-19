# Comando para iniciar os testes no unittest:       python -m unittest _tests/test_easyLogin.py
# Comando para gerar relatório do Allure:           pytest --alluredir=./_tests/_reports/_allureReports/_reportEasyLogin/
# Comando para abrir relatórios gerados no Allure:  allure serve ./_tests/_reports/_allureReports/_reportEasyLogin/

import unittest
import pytest
from _webDriver.WebDriver import Driver
from _pageObjects.easyLogin import EasyLogin
from _pageObjects.easyDashboard import EasyDashboard
from _pageObjects.easyMenu import EasyMenu
from _pageObjects.easyCustomerRegistration import EasyCustomerRegistration as ECR

class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()

    def tearDown(self):
        self.driver.instance.quit()

    #@unittest.skip("Não é um teste.")
    @pytest.mark.skip(reason="No need test this.")
    def test_login(self):
        launchEasyLogin = EasyLogin(self.driver.instance)
        launchEasyLogin.easyLogin()
        assert launchEasyLogin.is_logged()
   
    def test_customerRegistration(self):
        self.test_login()
        menu = EasyMenu(self.driver.instance)
        menu.openCustomerRegistrations()
        registration = ECR(self.driver.instance)
        assert registration.is_br_registration()      