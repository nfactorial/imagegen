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

from PIL import Image
from .image_block import ImageBlock


class OutputImage:
    """
    This class is used to provide a simple interface for creating
    and saving an image within the package.
    """
    def __init__(self, width, height):
        """
        Prepares the source image for use by the application.
        :param width: The width of the image (in pixels)
        :param height: The height of the image (in pixels)
        """
        self.size = (width, height)
        self.image = Image.new('RGB', self.size, 'black')

    def show(self):
        """
        Opens the image in an application so the user may view it.
        """
        self.image.show()

    def save(self, path):
        """
        Saves the image using the specified filename.
        :param path: The filename under which the image is to be saved.
        """
        self.image.save(path)

    @property
    def width(self):
        """
        Retrieves the width of the image in pixels.
        :return: The width of the image in pixels.
        """
        return self.size[0]

    @property
    def height(self):
        """
        Retrieves the height of the image in pixels.
        :return: The height of the image in pixels.
        """
        return self.size[1]

    def set_pixel(self, pos, color):
        """
        Sets the color of a specified pixel within the image.
        :param pos: x,y tuple containing the pixel coordinates to be set.
        :param color: The color to be stored at the specified pixel location.
        """
        self.image.putpixel(pos, (int(color.red * 255),
                                  int(color.green * 255),
                                  int(color.blue * 255)))

    def generate_blocks(self, block_size):
        """
        Generates a list of ImageBlock objects that may be used to generate the entire image.
        :param block_size: The size of a single image block (in pixels).
        :return: Yields an ImageBlock object for each section of the image.
        """
        x = 0
        while x < self.size[0]:
            y = 0
            while y < self.size[1]:
                yield ImageBlock(self, (x, y), (min(block_size, self.size[0] - x),
                                                min(block_size, self.size[1] - y)))
                y += block_size
            x += block_size
