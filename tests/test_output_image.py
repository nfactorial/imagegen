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
from imagegen.output_image import OutputImage


class TestSourceImage(unittest.TestCase):
    def test_block_size_1x1(self):
        image = OutputImage(1, 1)
        blocks = [x for x in image.generate_blocks(32)]
        self.assertEqual(1, len(blocks))

    def test_block_sise_64x64(self):
        image = OutputImage(64, 64)
        blocks = [x for x in image.generate_blocks(32)]
        self.assertEqual(4, len(blocks))
