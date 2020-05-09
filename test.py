import time
import requests
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


class UITesting(unittest.TestCase):

    redirection_delay = 3
    registered_user = 'UI_test'

    def setUp(self):
        chrome_options = Chrome_Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", desired_capabilities=chrome_options.to_capabilities())
        self.addCleanup(self.browser.quit)

    def testLogin(self):
        # Go to Login Page
        self.browser.get('http://192.168.1.115:3000')
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
        self.browser.get('http://192.168.1.115:3000/register')
        # Enter non-existing username
        username = self.browser.find_element_by_id('username')
        username.send_keys(self.registered_user)
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

    def tearDown(self):
        requests.get('http://192.168.1.115:8000/delete-test-registered-user/')


class GoogleChromeCompatibility(UITesting):

    registered_user = 'UI_Chrome_test'

    def setUp(self):
        chrome_options = Chrome_Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Remote(command_executor="http://selenium:4444/wd/hub", desired_capabilities=chrome_options.to_capabilities())
        self.addCleanup(self.browser.quit)


class FirefoxCompatibility(UITesting):

    registered_user = 'UI_Firefox_test'

    def setUp(self):
        firefox_options = Firefox_Options()
        firefox_options.add_argument("--headless")
        self.browser = webdriver.Remote(command_executor="http://selenium-firefox:4444/wd/hub", desired_capabilities=firefox_options.to_capabilities())
        self.addCleanup(self.browser.quit)


if __name__ == '__main__':
    unittest.main()
