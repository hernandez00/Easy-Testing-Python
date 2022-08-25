# Botão "Cotação":  //h4[text() = 'COTAÇÃO']

from selenium.webdriver.common.by import By


class DashboardObjects(object):

    btn_cotation = (By.XPATH, "//h4[text() = 'COTAÇÃO']")
