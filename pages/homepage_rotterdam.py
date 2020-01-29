from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePageRotterdam:

    def __init__(self, browser):
        self.browser = browser

    # def accept_cookie(self):
    #     button = WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//button[@ class = 'wol-acceptButton-module__button___eJm9c wol-cookies-module__btn_acceptAll___2IgCc']")))
    #     button.click()

    def homepage_rotterdam_element(self):
        title_elem = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='mainContainer']/div[3]/div[1]/div[1]/h1")))
        title_city = title_elem.text
        print(title_city)
        return title_city

    def new_homepage_url(self):
        url_new_homepage = self.browser.current_url
        print("Current URL: " + url_new_homepage)
        return url_new_homepage
