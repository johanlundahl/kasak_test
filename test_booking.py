from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import test_config as config
import test_login as access
import test_search as search
import method_chaining
from booking import Book
from datetime import datetime, timedelta
import time
import requests

class Booking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        access.login(self.driver)
        self.driver.find_element(By.XPATH, '//a[text()="Ny bokning"]').click()
        self.wait = WebDriverWait(self.driver, 2)

    def test_booking_required_parameters(self):
        book_btn = self.driver.find_element_by_id('button-direct')
        self.assertEqual(False, book_btn.is_enabled())
        self.driver.find_element_by_id('bookingCarRegistration').send_keys('TST101')
        
        self.wait.until(ec.element_to_be_clickable((By.ID,'button-direct')))
        book_btn = self.driver.find_element_by_id('button-direct')
        self.assertEqual(True, book_btn.is_enabled())
    
    def test_default_parameters(self):
        today_str = datetime.now().strftime('%Y-%m-%d')
        default_date = self.driver.find_element_by_id('datetimepicker').get_attribute('value')
        self.assertEqual(today_str, default_date)
        
        default_pickup = self.driver.find_element_by_id('pickup').is_selected()
        self.assertTrue(default_pickup)
        default_pickup_time = self.driver.find_element_by_id('bookingPickupTime').get_attribute('value')
        self.assertEqual('08:00', default_pickup_time)
        default_return_time = self.driver.find_element_by_id('bookingReturnTime').get_attribute('value')
        self.assertEqual('12:00', default_return_time)
        
        self.driver.find_element_by_id('recurrent').click()
        default_recurring_interval = self.driver.find_element_by_id('recurrentWeeks').get_attribute('value')
        self.assertEqual('4', default_recurring_interval)
        default_recurrences = self.driver.find_element_by_id('recurrentTimes').get_attribute('value')
        self.assertEqual('6', default_recurrences)
        
    def test_add_minimal_booking_without_customer(self):
        today_str = datetime.now().strftime('%Y-%m-%d')
        self.driver.find_element_by_id('datetimepicker').send_keys(today_str)
        self.driver.find_element_by_id('bookingPickupTime').send_keys('0915')
        self.driver.find_element_by_id('bookingReturnTime').send_keys('1145')
        self.driver.find_element_by_id('bookingCarRegistration').send_keys('TST101')
        
        self.wait.until(ec.element_to_be_clickable((By.ID,'button-direct')))        
        book_btn = self.driver.find_element_by_id('button-direct')
        self.assertEqual(True, book_btn.is_enabled())
        self.driver.find_element_by_id('button-direct').click()
        
        # verify that booking was successful
        date_picker = self.driver.find_element_by_id('datetimepicker')
        self.assertEqual(today_str, date_picker.get_attribute('value'))
    
    def test_directs_to_booked_day_in_overview(self):
        tomorrow = datetime.now() + timedelta(days=1)
        day_str = tomorrow.strftime('%Y-%m-%d')
        
        self.driver.find_element_by_id('datetimepicker').clear()
        self.driver.find_element_by_id('datetimepicker').click()
        self.driver.find_element_by_id('datetimepicker').send_keys(day_str)
        self.driver.find_element_by_id('datetimepicker').send_keys(Keys.TAB)
        
        self.driver.find_element_by_id('bookingPickupTime').send_keys('0911')
        self.driver.find_element_by_id('bookingReturnTime').send_keys('1145')
        self.driver.find_element_by_id('bookingCarRegistration').send_keys('TST102')
        
        book_btn = self.wait.until(ec.element_to_be_clickable((By.ID,'button-direct')))        
        book_btn.click()
        
        # verify that booking was successful
        self.assertTrue('Översikt' in self.driver.title)
        date_picker = self.driver.find_element_by_id('datetimepicker')
        self.assertEqual(day_str, date_picker.get_attribute('value'))
    
    def test_add_recurrent_booking(self):
        today_str = datetime.now().strftime('%Y-%m-%d')
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=3)
        self.driver.find_element_by_id('datetimepicker').send_keys(today_str)
        
        self.driver.find_element_by_id('bookingPickupTime').send_keys(start_time.strftime('%H%M'))
        self.driver.find_element_by_id('bookingReturnTime').send_keys(end_time.strftime('%H%M'))
        self.driver.find_element_by_id('bookingCarRegistration').send_keys('TST103')
        
        self.driver.find_element_by_id('recurrent').click()
        self.driver.find_element_by_id('recurrentWeeks').clear()
        self.driver.find_element_by_id('recurrentWeeks').send_keys('2')
        self.driver.find_element_by_id('recurrentTimes').clear()
        self.driver.find_element_by_id('recurrentTimes').send_keys('2')
        
        book_btn = self.wait.until(ec.element_to_be_clickable((By.ID,'button-direct')))        
        self.assertEqual(True, book_btn.is_enabled())
        book_btn.click()
        
        response = requests.get(url = 'http://89.160.52.144/Kasak/server/public/api/search/{}%20{}'.format(today_str, 'TST103'))
        self.assertTrue(len(response.json()) > 0)
        
    @unittest.skip('')
    def test_add_booking_with_existing_customer(self):
        pass
    
    @unittest.skip('')
    def test_add_booking_with_new_customer(self):
        pass
    
    def tearDown(self):
        access.logout(self.driver)
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()