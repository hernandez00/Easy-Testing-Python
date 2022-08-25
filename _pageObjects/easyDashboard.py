from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from _pageObjects._locators.dashboardLocators import DashboardObjects
from _pageObjects.baseMethod import Base


class EasyDashboard(Base):

    def easyDashboardCotation(self):
        btn_cotation = Base.find_element(
            self._driver, DashboardObjects.btn_cotation)
        btn_cotation.click()
