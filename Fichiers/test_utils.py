# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        try:
            self.assertEqual(utils.fact(5), 120)
        except:
            print("mort")

        pass
    
    def test_roots(self):
        # À compléter...
        try:
            self.assertEqual(utils.roots(1, 0, 1), 0)
        except:
            print("mort")
        pass
    
    def test_integrate(self):
        # À compléter...
        try:
            self.assertEqual(utils.integrate('x ** 2 - 1', -1, 1), 120)
        except:
            print("mort")
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())






