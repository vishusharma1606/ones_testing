from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main import SeleniumTest

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.lp = SeleniumTest()
        self.lp.setUp()
        
    def test_search1(self):
        self.lp.testsearch1()
        
    def test_search2(self):
        self.lp.testsearch2()
        
    def test_search3(self):
        self.lp.testsearch3()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
    unittest.TextTestRunner(verbosity=2).run(suite)
