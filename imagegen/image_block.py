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

from color import Color
from eval_info import EvalInfo
from sampler_base import SamplerBase


class ImageBlock:
    """
    Represents a rectangular subset of pixels within an image.
    Used to specify which pixels a particular task should be generating.
    """
    def __init__(self, pos, size, image_size):
        """
        :param pos: The pixel position within the image where the top left of the image block begins.
        :param size: Tuple containing the width and height (in pixels) of the image block.
        """
        self.pos = pos
        self.size = size
        self.image_size = image_size

    @property
    def x(self):
        """
        Gets the position along the horizontal axis of the image block object.
        :return: The position along the horizontal axis of the image block.
        """
        return self.pos[0]

    @property
    def y(self):
        """
        Gets the position along the vertical axis of the image block object.
        :return: The position along the vertical axis of the image block.
        """
        return self.pos[1]

    @property
    def width(self):
        """
        Gets the width (in pixels) of the image block object.
        :return: The width (in pixels) of the image block.
        """
        return self.size[0]

    @property
    def height(self):
        """
        Gets the height (in pixels) of the image block object.
        :return: The height (in pixels) of the image block object.
        """
        return self.size[1]

    def next_pixel(self):
        """
        Generator function that returns the coordinates of each pixel within the ImageBlock object.
        :return: The next pixel within the image block that should be processed.
        """
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                yield (self.pos[0] + x, self.pos[1] + y)

    def execute(self, image, output):
        """
        Evaluates the color of each pixel contained within this image block.
        :param image: The image whose content we're evaluating.
        :param output: The output node we're performing the evaluation for.
        """
        # TODO: The sampler will be specified in the definition file
        sampler = SamplerBase(1, 1, (1.0, 1.0))

        eval_info = EvalInfo(output.node)
        for pixel in self.next_pixel():
            image.set_pixel(pixel, self.evaluate_pixel(pixel, eval_info, sampler))

    def evaluate_pixel(self, pixel, info, sampler):
        """
        Computes the color of a pixel within the image block.
        :param pixel: Coordinates of the pixel being evaluated.
        :param info: EvalInfo object describing the sample being evaluated.
        :param sampler: The sampler to be used when computing the pixel color.
        :return: The color of the specified pixel.
        """
        # TODO: Move color object into info, so we don't need to construct one all the time?
        color = Color()
        for info.x, info.y in sampler.next_sample(pixel):
            info.x /= self.image_size[0]
            info.y /= self.image_size[1]
            color += info.node.evaluate(info)

        return color / len(sampler)
