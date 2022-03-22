
import unittest 
import datetime

from support_functions import Challenge_tools as ct


class TestSeason(unittest.TestCase):

    def testRandom(self):
        
        self.assertEqual(ct.get_season(datetime.date(2016, 2, 21)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 3, 19)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 12, 20)) , 'Fall')
        self.assertEqual(ct.get_season(datetime.date(2016, 11, 10)) , 'Fall')
        self.assertEqual(ct.get_season(datetime.date(2016, 8, 19)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 7, 25)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 6, 23)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 5, 20)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 4, 10)) , 'Spring')

    def test_critical_20(self):
        self.assertEqual(ct.get_season(datetime.date(2016, 12, 20)) , 'Fall')
        self.assertEqual(ct.get_season(datetime.date(2016, 3, 20)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 6, 20)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 9, 20)) , 'Summer')

    def test_critical_21(self):
        self.assertEqual(ct.get_season(datetime.date(2016, 12, 21)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 3, 21)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 6, 21)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 9, 21)) , 'Fall')
    
    def test_non_critical_20(self):
        self.assertEqual(ct.get_season(datetime.date(2016, 1, 20)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 2, 20)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 4, 20)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 5, 20)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 7, 20)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 8, 20)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 10, 20)) , 'Fall')
        self.assertEqual(ct.get_season(datetime.date(2016, 11, 20)) , 'Fall')


    def test_non_critical_21(self):
        self.assertEqual(ct.get_season(datetime.date(2016, 1, 21)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 2, 21)) , 'Winter')
        self.assertEqual(ct.get_season(datetime.date(2016, 4, 21)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 5, 21)) , 'Spring')
        self.assertEqual(ct.get_season(datetime.date(2016, 7, 21)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 8, 21)) , 'Summer')
        self.assertEqual(ct.get_season(datetime.date(2016, 10, 21)) , 'Fall')
        self.assertEqual(ct.get_season(datetime.date(2016, 11, 21)) , 'Fall')    

if __name__ == '__main__':
    
    unittest.main()



    

