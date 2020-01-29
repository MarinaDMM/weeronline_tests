import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    URL = 'https://www.weeronline.nl/'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def accept_cookie(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[@ class = 'wol-acceptButton-module__button___eJm9c wol-cookies-module__btn_acceptAll___2IgCc']")))
        button.click()

    def get_weerbericht_link(self):
        element = self.browser.find_elements_by_xpath("//*[contains(text(), 'Weerbericht Nederland')]")[0]
        self.browser.execute_script("arguments[0].click();", element)

    def search(self):
        search_icon = self.browser.find_elements_by_xpath(".//img[@class = 'wol-icon-module__icon___1sIwS']")[0]
        self.browser.execute_script("arguments[0].click();", search_icon)
