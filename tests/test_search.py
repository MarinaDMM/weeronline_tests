from pages.home import *
from pages.search_page import *
from pages.weer_rotterdam import *
from selenium import webdriver
import pytest
from time import sleep



@pytest.fixture
def browser():
    '''Browser Chrome'''
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


city = 'Rotterdam'


class TestSearch:
    def test_search(self, browser):
        home_page = HomePage(browser)
        search_page = SearchPage(browser)
        rotterdam_page = WeerRotterdamPage(browser)
        home_page.load()
        home_page.search()
        sleep(3)
        search_page.accept_cookie()
        sleep(3)
        search_page.enter_city(city)
        sleep(3)
        search_page.first_city()
        sleep(3)
        city_actuall = rotterdam_page.rotterdam_check()

        assert city == city_actuall,  'Error: can not find Rotterdam'



