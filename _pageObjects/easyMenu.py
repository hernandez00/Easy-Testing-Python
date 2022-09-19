from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pageObjects.baseMethod import Base
from _pageObjects._locators.menu import MenuObjects


class EasyMenu(Base):

    def easyMenu(self):
        btn_menu = Base.find_element(
            self._driver, MenuObjects.BTN_MENU).click()
    
    def openCustomerRegistrations(self):
        self.easyMenu()
        
        btn_registrations = Base.find_element(
            self._driver, MenuObjects.MENU_ITEM_RECORDS).click()
        
        btn_brazilianCustomer = Base.find_element(
            self._driver, MenuObjects.SUBITEM_BR_CLIENT).click()