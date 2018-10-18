from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import test_config as config

class Access(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_access_requires_login(self):
        self.driver.get('{}/Kasak/client/htdocs/carStatus.php'.format(config.url))
        heading = self.driver.find_element(By.XPATH, '//h1[text()="Logga in"]')
        self.assertTrue(heading is not None)
    
    def test_load_login(self):
        self.driver.get(config.url)
        try:
            usr = self.driver.find_element_by_name('username')
            pwd = self.driver.find_element_by_name('password')
        except NoSuchElementException:
            self.fail('Input fields were not found.')

    def test_login(self):
        login(self.driver)
        usr = self.driver.find_element_by_id('navbarDropdown')
        self.assertEqual('Inloggad: admin', usr.text)
        
    def test_logout(self):
        login(self.driver)
        logout(self.driver)
        try:
            heading = self.driver.find_element(By.XPATH, '//h1[text()="Logga in"]')
        except NoSuchElementException:
            self.fail('Cannot find login title')
    
    def tearDown(self):
        self.driver.close()

def login(driver):
    driver.get(config.url)
    driver.find_element_by_name('username').send_keys(config.usr_admin)
    driver.find_element_by_name('password').send_keys(config.pwd_admin)
    driver.find_element(By.XPATH, '//input[@value="Logga in"]').click()

def logout(driver):
    driver.find_element_by_id('navbarDropdown').click()
    driver.find_element(By.XPATH, '//a[text()="Logga ut"]').click()
        
if __name__ == '__main__':
    unittest.main()