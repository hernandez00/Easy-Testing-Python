# Menu Hamburger:      //und-menu-outlined-icon[@class = 'text-white menu-icon']
# Botão Cadastros:     //span[contains(text(), "Cadastros")]

from selenium.webdriver.common.by import By


class MenuObjects(object):

    BTN_MENU = (By.XPATH, "//und-menu-outlined-icon[@class = 'text-white menu-icon']")
    
    MENU_ITEM_RECORDS = (By.XPATH, "//li[2]/div")
    SUBITEM_BR_CLIENT = (By.XPATH, "//li[2]/ul/li/div")