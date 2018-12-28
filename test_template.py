from selenium import webdriver
import unittest

class YourTestCase(unittest.TestCase):

    # will be called before all tests in this class
    @classmethod
    def setUpClass(cls):
        pass

    # will be called before each test in this class
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_of_something(self):
        self.driver.get('http://a/url/to/get')
        heading = self.driver.find_element_by_name('heading')
        self.assertTrue(heading is not None)
        
    def test_of_something_else(self):
        self.driver.get('http://another/url/to/get')
        # do something
        # assert something
        
    # will be called after each test in this class
    def tearDown(self):
        self.driver.close()
        
    # will be called after all tests in this class
    @classmethod
    def tearDownClass(cls):
        pass
        
if __name__ == '__main__':
    unittest.main()