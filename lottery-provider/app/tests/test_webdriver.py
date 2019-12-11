from app.src.webdriver import Webdriver
from selenium.webdriver.common.keys import Keys


class TestWebdriver():
    def test_creation_webdriver(self):
        webdriver = Webdriver()

        assert webdriver.driver

        webdriver.driver.close()

    def test_url_connection(self):
        webdriver = Webdriver()

        webdriver.get_lottery_game_webpage('mega-sena')
        assert 'Yahoo' in webdriver.driver.title

        webdriver.driver.close()

    def test_page_element_find(self):
        webdriver = Webdriver()

        webdriver.driver.get('http://www.yahoo.com')

        # Find the search box
        elem = webdriver.driver.find_element_by_id('uh-search-box')
        elem.send_keys('seleniumhq' + Keys.RETURN)

        result_not_found = webdriver.driver.find_element_by_class_name(
            'first last')
        assert not result_not_found

        webdriver.driver.close()
