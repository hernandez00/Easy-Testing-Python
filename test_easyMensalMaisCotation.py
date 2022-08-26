# Comando para iniciar os testes no unittest:       python -m unittest _tests/test_easyLogin.py
# Comando para gerar relatório do Allure:           pytest --alluredir=./_tests/_reports/_allureReports/_reportEasyLogin/
# Comando para abrir relatórios gerados no Allure:  allure serve ./_tests/_reports/_allureReports/_reportEasyLogin/

import unittest
import pytest
from _webDriver.WebDriver import Driver
from _pageObjects.easyLogin import EasyLogin
from _pageObjects.easyDashboard import EasyDashboard


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
   
    def test_openCotation(self):
        self.test_login()
        cotation = EasyDashboard(self.driver.instance)
        cotation.openCotation()
        assert cotation.is_cotation()
        