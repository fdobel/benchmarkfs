
import unittest
import numpy as np
from funcs.ackley import ackley


class Test(unittest.TestCase):

    def test_check_value_1(self):
        value = ackley(np.zeros(2))
        self.assertEqual(value, 0.0)

    def test_check_value_2(self):
        value = ackley(np.array([1, 2]))
        self.assertEqual(value, -41.17669169414491)

    def test_check_value_3(self):
        value = ackley(np.array([0.5, 0.5]))
        self.assertEqual(value, -6.13197800233203)

    def test_check_value_4(self):
        value = ackley(np.array([-0.15, 0.15]))
        self.assertEqual(value, -1.3196211942873575)
