from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self):
        self.instance = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        #webdriver.ChromeOptions.add_argument(self, argument)
        self.instance.get("https://easy.hml.unidas.com.br/login")
