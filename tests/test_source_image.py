# test_source_image.py

import unittest
from imagegen.source_image import SourceImage


class TestSourceImage(unittest.TestCase):
    def test_block_size_1x1(self):
        image = SourceImage(1, 1)
        blocks = [x for x in image.generate_blocks(32)]
        self.assertEqual(1, len(blocks))

    def test_block_sise_64x64(self):
        image = SourceImage(64, 64)
        blocks = [x for x in image.generate_blocks(32)]
        self.assertEqual(4, len(blocks))
