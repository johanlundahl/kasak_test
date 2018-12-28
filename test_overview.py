from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
import test_config as config
import test_login as access
import test_search as search
from datetime import datetime, timedelta
from booking import Book

class Overview(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        access.login(self.driver)
        self.driver.find_element(By.XPATH, '//a[text()="Översikt"]').click()

    def test_defaults_to_today(self):
        today_str = datetime.now().strftime('%Y-%m-%d')
        date_picker = self.driver.find_element_by_id('datetimepicker')
        self.assertEqual(today_str, date_picker.get_attribute('value'))
    
    def test_move_to_next_day(self):
        self.driver.find_element_by_id('nextDay').click()
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%Y-%m-%d')
        date_picker = self.driver.find_element_by_id('datetimepicker')
        self.assertEqual(tomorrow_str, date_picker.get_attribute('value'))
    
    def test_move_to_prev_day(self):
        self.driver.find_element_by_id('prevDay').click()
        yesterday = datetime.now() + timedelta(days=-1)
        yesterday_str = yesterday.strftime('%Y-%m-%d')
        date_picker = self.driver.find_element_by_id('datetimepicker')
        self.assertEqual(yesterday_str, date_picker.get_attribute('value'))
    
    @unittest.skip('')
    def test_show_morning(self):
        b = Book().car('TST101').with_package('Bas').at('2018-05-31').collect_at('0915').return_at('11.45')
        self.driver.find_element(By.XPATH, '//label[input/@value="am"]').click()
        rows = self.driver.find_elements(By.XPATH, '//table[@id="car-status-table"]//tr[@id]')
        pass
    
    @unittest.skip('')
    def test_show_afternoon(self):
        self.driver.find_element(By.XPATH, '//label[input/@value="pm"]').click()
        rows = self.driver.find_elements(By.XPATH, '//table[@id="car-status-table"]//tr[@id]')
        pass
    
    @unittest.skip('')
    def test_show_all_day(self):
        self.driver.find_element(By.XPATH, '//label[input/@value="all"]').click()
        rows = self.driver.find_elements(By.XPATH, '//table[@id="car-status-table"]//tr[@id]')
        # assert on number of rows
        self.fail('not implemented...')
    
    @unittest.skip('')
    def test_view_details(self):
        
        pass
    
    @unittest.skip('')
    def test_add_comment(self):
        pass
    
    @unittest.skip('')
    def test_set_collected(self):
        pass
    
    @unittest.skip('')
    def test_regret_collected(self):
        pass
    
    @unittest.skip('')
    def test_set_returned(self):
        pass
    
    @unittest.skip('')
    def test_regret_returned(self):
        pass
    
    def tearDown(self):
        #ok = self.currentResult.wasSuccessful()
        #errors = self.currentResult.errors
        #failures = self.currentResult.failures
        #res = ''
    
        access.logout(self.driver)
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()