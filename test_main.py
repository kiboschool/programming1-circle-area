import unittest
from main import *

class Test(unittest.TestCase):
    def test_area_circle(self):
        # so that 3.14 for pi still passes
        # quite loose with matching
        # and looser as r increases
        self.assertAlmostEqual(area_circle(0.1), 0.031415, 3)
        self.assertAlmostEqual(area_circle(1), 3.1415, 2)
        self.assertAlmostEqual(area_circle(5), 78.539816, 1)
        self.assertAlmostEqual(area_circle(16.2), 824.4795, 0)

if __name__ == '__main__':
    unittest.main()
