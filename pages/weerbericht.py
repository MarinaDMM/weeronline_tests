from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WeerberichtPage:

    def __init__(self, browser):
        self.browser = browser

    # def accept_cookie(self):
    #     button = WebDriverWait(self.browser, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ".//button[@ class = 'swol-acceptButton-module__button___eJm9c wol-cookies-module__btn_acceptAll___2IgCc']")))
    #     button.click()

    def get_url_actual(self):
        url_actual = self.browser.current_url
        print("Current URL: " + url_actual)
        return url_actual

