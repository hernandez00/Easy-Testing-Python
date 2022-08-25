from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pageObjects._locators.loginLocators import LoginObjects
from _pageObjects._locators.dashboardLocators import DashboardObjects
from _pageObjects.baseMethod import Base


class EasyLogin(Base):

    def easyLogin(self):
        edit_document = Base.find_element(
            self._driver, LoginObjects.EDIT_DOCUMENT)
        edit_document.send_keys('46435591873')

        edit_password = Base.find_element(
            self._driver, LoginObjects.EDIT_PASSWORD)
        edit_password.send_keys('teste123')

        btn_login = Base.find_element(self._driver, LoginObjects.BTN_LOGIN)
        btn_login.click()

    def is_logged(self):
        is_logged = Base.verify_title(self._driver, "Dashboard")
        if is_logged:
            print("Login realizado com sucesso!")
        else:
            print("Algo deu errado!")
        return is_logged
