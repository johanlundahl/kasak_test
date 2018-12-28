from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import test_config as config
import test_login as access

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        access.login(self.driver)
        self.driver.find_element(By.XPATH, '//a[text()="Sök"]').click()
        
    def test_find_booking(self):
        #start test by adding booking
        elm = find_booking(self.driver, 'RCO 038', '2018-05-28')
        self.assertTrue(elm is not None)   
    
    def test_find_customer(self):
        #start test by adding customer
        elm = find_customer(self.driver, 'BUS')
        self.assertTrue(elm is not None)   
    
    def tearDown(self):
        access.logout(self.driver)
        self.driver.close()

def find_booking(driver, reg_nbr, date):
    try:
        driver.find_element_by_name('search').send_keys(reg_nbr)
        driver.find_elements(By.XPATH, '//button[//text()="Sök"]')
        bookings = driver.find_elements(By.XPATH, '//tr[td/h4/text()="{}" and td/h4/text()="{}"]'.format(reg_nbr, date))
        return bookings[0] if len(bookings) > 0 else None 
    except NoSuchElementException:
        return None

def find_customer(driver, name):
    try:
        driver.find_element_by_name('search').send_keys(name)
        driver.find_element(By.XPATH, '//label[input/@value="customers"]').click()
        driver.find_elements(By.XPATH, '//button[//text()="Sök"]')
        bookings = driver.find_elements(By.XPATH, '//tr[td/h5/text()="{}"]'.format(name))
        return bookings[0] if len(bookings) > 0 else None 
    except NoSuchElementException:
        return None
    
if __name__ == '__main__':
    unittest.main()