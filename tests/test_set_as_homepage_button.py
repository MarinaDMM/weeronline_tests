from pages.home import *
from pages.homepage_rotterdam import *
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
Url_home = 'https://www.weeronline.nl/'


class TestSetAsHomepageButton:
    def test_new_homepage(self, browser):
        rotterdam_page = WeerRotterdamPage(browser)
        new_home_page = HomePageRotterdam(browser)
        rotterdam_page.load()
        sleep(3)
        rotterdam_page.accept_cookie()
        sleep(3)
        rotterdam_page.set_page_as_homepage()
        sleep(3)
        rotterdam_page.press_weeronline()
        sleep(3)
        # new_home_page.accept_cookie()
        # sleep(20)
        new_page_city = new_home_page.homepage_rotterdam_element()
        sleep(10)

        assert city == new_page_city, 'Error: can not find Rotterdam'
        sleep(15)
        assert Url_home == new_home_page.new_homepage_url(), 'Error: correct URL  is not found'
