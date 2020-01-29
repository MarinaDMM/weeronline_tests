from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainLocators
from time import sleep


class WeerRotterdamPage:
    URL_rotterdam = 'https://www.weeronline.nl/Europa/Nederland/Rotterdam/4057931'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL_rotterdam)

    def accept_cookie(self):
        button = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, ".//button[@ class = 'wol-acceptButton-module__button___eJm9c wol-cookies-module__btn_acceptAll___2IgCc']")))
        button.click()

    def rotterdam_check(self):
        element = self.browser.find_elements_by_xpath("//*[@id='mainContainer']/div[1]/div/div/div[1]/a[3]/div/div/span")[0]
        value = element.text
        print("The value is " + value)
        return value

    def set_page_as_homepage(self):
        set_as_homepage = self.browser.find_elements_by_xpath("//*[@id='mainContainer']/div[4]/div/div/a/div/div/span")[0]
        self.browser.execute_script("arguments[0].click();", set_as_homepage)

    def press_weeronline(self):
        weeronline = self.browser.find_elements_by_xpath("//*[contains(text(), 'Weeronline')]")[0]
        self.browser.execute_script("arguments[0].click();", weeronline)
