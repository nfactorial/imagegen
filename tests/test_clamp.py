"""
Copyright 2016 nfactorial

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
from imagegen.math_help import clamp


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
