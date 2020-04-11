
import unittest
import numpy as np
from funcs.rastrigin import rastrigin


class Test(unittest.TestCase):

    def test_check_value_1(self):
        value = rastrigin(np.zeros(2))
        self.assertEqual(value, 0.0)

    def test_check_value_2(self):
        value = rastrigin(np.array([1, 2, 3]))
        self.assertEqual(value, 14.0)

    def test_check_value_3(self):
        value = rastrigin(np.array([0.5, 0.5, 0.5]))
        self.assertEqual(value, 60.75)

    def test_check_value_4(self):
        value = rastrigin(np.array([-0.15, 0.15, 0.3, -0.2]))
        self.assertEqual(value, 28.419294954150534)
