import unittest
from test_booking import Booking
from test_login import Access
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Access('test_access_requires_login'))
    suite.addTest(Access('test_load_login'))
    suite.addTest(Access('test_login'))
    suite.addTest(Access('test_logout'))

    suite.addTest(Booking('test_booking_required_parameters'))
    suite.addTest(Booking('test_default_parameters'))
    suite.addTest(Booking('test_add_minimal_booking_without_customer'))
    suite.addTest(Booking('test_directs_to_booked_day_in_overview'))
    suite.addTest(Booking('test_add_recurrent_booking'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())