import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


class PairsCrawler:
    TARGET_URL: str = 'https://pairs.lv'

    _driver = None

    _min_sleep_second = None

    _max_sleep_second = None


    def __init__(self, min_sleep_second, max_sleep_second):
        # options = webdriver.ChromeOptions()
        self._driver = webdriver.Chrome()
        self._driver.implicitly_wait(10)

        self._min_sleep_second = min_sleep_second
        self._max_sleep_second = max_sleep_second

    def auth(self, login_id, login_passwprd):
        self._driver.get(self.TARGET_URL)

        login_button = self._driver.find_element_by_css_selector('button[class$="FacebookLoginButton"]')
        login_button.click()

        # 開いているウィンドウのリスト
        handls = self._driver.window_handles
        self._driver.switch_to.window(handls[1])

        id_input = self._driver.find_element_by_id('email')
        id_input.send_keys(login_id)
        pass_input = self._driver.find_element_by_id('pass')
        pass_input.send_keys(login_passwprd)
        pass_input.submit()

        self._driver.switch_to.window(handls[0])

    def profile_list(self):
        self.random_wait()

        for i in range(2):
            dialoga_pannel = self._driver.find_elements_by_css_selector('div[class$="DialogAppeal"]')
            if dialoga_pannel:
                dialoga_pannel[0].find_element_by_css_selector('button[class$="pointerStyles-TextButton-DialogAppeal"]').click()

            search_link = self._driver.find_element_by_css_selector('a[href="/search"]')
            search_link.click()
            self.random_wait()


    def crawle(self, max_view_profile_count):
        action_chains = ActionChains(self._driver)

        count = len(self._driver.find_elements_by_css_selector('button[class$="GridUserItem"]'))
        max_scroll_count: int = max_view_profile_count // count
        for i in range(max_scroll_count):
            bottom = self._driver.find_element_by_css_selector('div[id$="dialog-root"]')
            action_chains.move_to_element(bottom)
            action_chains.perform()
            self.random_wait()

        profile_link = self._driver.find_element_by_css_selector('a[href^="/user/profile/search/grid/"]')
        action_chains.move_to_element(profile_link)
        profile_link.click()
        self.random_wait()

        for i in range(max_view_profile_count - 1):
            next_link = self._driver.find_element_by_link_text('次のお相手を見る')
            action_chains.move_to_element(next_link)
            next_link.click()
            self.random_wait()

    def random_wait(self):
        second = random.uniform(self._min_sleep_second, self._max_sleep_second)
        time.sleep(second)
