import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class GoogleChromeTestCase(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
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
        time.sleep(2)
        # Redirect to Inventory List page
        inventory_list = self.browser.find_element_by_id('book-inventory')

    def testRegister(self):
        # Go to Registration Page
        self.browser.get('http://192.168.1.115:3000/register')
        # Enter non-existing username
        username = self.browser.find_element_by_id('username')
        username.send_keys('UI_test')
        # Enter password
        password = self.browser.find_element_by_id('password')
        password.send_keys('pass1234')
        # Enter confirmation password
        confirm_password = self.browser.find_element_by_id('confirm_password')
        confirm_password.send_keys('pass1234')
        # Click Register
        register_button = self.browser.find_element_by_id('register-button')
        register_button.click()
        time.sleep(2)
        # Redirect to Inventory List page
        inventory_list = self.browser.find_element_by_id('book-inventory')

if __name__ == '__main__':
    unittest.main(verbosity=2)