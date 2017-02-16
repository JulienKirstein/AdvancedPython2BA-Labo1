# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils
import program


class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(program.fact(2), 2)
        pass
    
    def test_roots(self):
        self.assertEqual(program.root(1), 1)
        pass
    
    def test_integrate(self):
        self.assertEqual(program.integrate(0), 0)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())