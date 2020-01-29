from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SearchPage:
    def __init__(self, browser):
        self.browser = browser

    def accept_cookie(self):
        button = WebDriverWait(self.browser, 60).until(
            EC.visibility_of_element_located((By.XPATH,
                                              ".//button[@ class = 'wol-acceptButton-module__button___eJm9c wol-cookies-module__btn_acceptAll___2IgCc']")))
        button.click()

    def enter_city(self, phrase):
        edit_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, ".//input[@type='text']"))
        )
        edit_field.clear()
        sleep(3)
        edit_field.send_keys(phrase)
        sleep(3)

    def first_city(self):
        first_element = self.browser.find_elements_by_xpath("//*[@id='root']/div/section/div[1]/div/ul/div[1]/li")[0]
        self.browser.execute_script("arguments[0].click();", first_element)




