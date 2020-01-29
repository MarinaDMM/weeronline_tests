from selenium.webdriver.common.by import By


class MainLocators(object):
    """A class for main page locators. All main page locators should come here"""
    SEARCH_INPUT = (By.CSS_SELECTOR, "ul.wol-suggestion-module__results___2Ltmh")
    # GO_BUTTON = (By.ID, 'sautocomplete-input')
