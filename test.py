import os
import time
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


class UITesting(unittest.TestCase):

    redirection_delay = 3
    host = os.environ.get('HOST', 'http://hga66883.com')
    api_host = os.environ.get('API_HOST', 'http://api.hga66883.com')

    def setUp(self):
        self.options.add_argument("--headless")
        self.browser = webdriver.Remote(
            command_executor=f"http://{self.selenium_server}:4444/wd/hub",
            desired_capabilities=self.options.to_capabilities())
        self.addCleanup(self.browser.quit)

    def testLogin(self):
        # Go to Login Page
        self.browser.get(f'{self.host}')
        # Enter Correct Username
        username = self.browser.find_element_by_id('username')
        username.send_keys('armadadean')
        # Enter Correct Password
        password = self.browser.find_element_by_id('password')
        password.send_keys('pass1234')
        # Click Login
        login_button = self.browser.find_element_by_id('login-button')
        login_button.click()
        time.sleep(self.redirection_delay)
        # Redirect to Inventory List page
        inventory_list = self.browser.find_element_by_id('book-inventory')

    def testRegister(self):
        # Go to Registration Page
        self.browser.get(f'{self.host}/register')
        # Enter non-existing username
        username = self.browser.find_element_by_id('username')
        username.send_keys(f'UI_{self.platform}_test')
        # Enter password
        password = self.browser.find_element_by_id('password')
        password.send_keys('pass1234')
        # Enter confirmation password
        confirm_password = self.browser.find_element_by_id('confirm_password')
        confirm_password.send_keys('pass1234')
        # Click Register
        register_button = self.browser.find_element_by_id('register-button')
        register_button.click()
        time.sleep(self.redirection_delay)
        # Redirect to Inventory List page
        inventory_list = self.browser.find_element_by_id('book-inventory')
        requests.get(f'{self.api_host}/'
                     f'delete-test-registered-user/'
                     f'?platform={self.platform}')


class GoogleChromeCompatibility(UITesting):

    selenium_server = "selenium-chrome"
    options = Chrome_Options()
    platform = 'Chrome'


class FirefoxCompatibility(UITesting):

    selenium_server = "selenium-firefox"
    options = Firefox_Options()
    platform = 'Firefox'


if __name__ == '__main__':
    unittest.main()
