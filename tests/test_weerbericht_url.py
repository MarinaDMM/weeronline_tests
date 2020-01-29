from time import sleep
from pages.home import *
from pages.weerbericht import *
from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    '''Browser Chrome'''
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


url_expected = 'https://www.weeronline.nl/weerbericht-nederland'


class TestAclueel():
    def test_weerbericht(self, browser):
        home_page = HomePage(browser)
        weerbericht = WeerberichtPage(browser)
        home_page.load()

        home_page.accept_cookie()
        home_page.get_weerbericht_link()
        sleep(5)
        actual_url = weerbericht.get_url_actual()

        assert url_expected == actual_url, 'Error: can not find Weerbericht page'
