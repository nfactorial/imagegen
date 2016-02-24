# test_clamp.py

import unittest
from imagegen.source_image import clamp


class TestClamp(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(0, clamp(-2, 0, 1))
        self.assertEqual(-50, clamp(-100, -50, 0))
        self.assertEqual(50, clamp(-100, 50, 100))

    def test_upper(self):
        self.assertEqual(1, clamp(2, 0, 1))
        self.assertEqual(50, clamp(1, 50, 100))
        self.assertEqual(50, clamp(-100, 50, 100))

    def test_center(self):
        test_val = 0.5
        self.assertEqual(test_val, clamp(test_val, 0, 1))
