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

from .color import Color
from .eval_info import EvalInfo
from .math_help import rotate_origin
from .sampler_base import SamplerBase
from .stochastic_sampler import StochasticSampler


class ImageBlock:
    """
    Represents a rectangular subset of pixels within an image.
    Used to specify which pixels a particular task should be generating.
    """
    def __init__(self, image, pos, size):
        """
        :param pos: Tuple contained the x, y position of the image block.
        :param size: Tuple containing the width and height (in pixels) of the image block.
        """
        self.image = image
        self.pos = pos
        self.size = size

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

    def execute(self, output):
        """
        Evaluates the color of each pixel contained within this image block.
        :param output: The output node we're performing the evaluation for.
        """
        # TODO: The sampler will be specified in the definition file
        sampler = SamplerBase(1, 1, (1.0, 1.0))
        # sampler = StochasticSampler(6, 6, (1.0, 1.0))

        eval_info = EvalInfo(output.node)
        eval_info.image_size = (output.width, output.height)
        eval_info.pixel_size = (1.0 / output.width, 1.0 / output.height)
        for pixel in self.next_pixel():
            self.image.set_pixel(pixel, self.evaluate_pixel(pixel, eval_info, sampler))

    def evaluate_pixel(self, pixel, info, sampler):
        """
        Computes the color of a pixel within the image block.
        :param pixel: Tuple containing x, y coordinates of the pixel being evaluated.
        :param info: EvalInfo object describing the sample being evaluated.
        :param sampler: The sampler to be used when computing the pixel color.
        :return: The color of the specified pixel.
        """
        # TODO: Move color object into info, so we don't need to construct one all the time?
        color = Color()
        for info.x, info.y in sampler.next_sample(pixel):
            info.x, info.y = rotate_origin((info.x * info.pixel_size[0] * info.node.scaling[0],
                                            info.y * info.pixel_size[1] * info.node.scaling[1]),
                                           (0.5, 0.5),      # TODO: Retrieve origin from node
                                           info.node.rotation)
            color += info.node.evaluate(info)
        return color / len(sampler)


def execute_block(block, output):
    """
    Evaluates the color of each pixel contained within this image block.
    This method is part of an investigation into using multiple processes
    and should not be used outside of that context.
    :param block: The block whose content is to be evaluated.
    :param output: The output node we're performing the evaluation for.
    """
    # TODO: The sampler will be specified in the definition file
    sampler = SamplerBase(1, 1, (1.0, 1.0))

    eval_info = EvalInfo(output.node)
    for pixel in block.next_pixel():
        block.image.set_pixel(pixel, block.evaluate_pixel(pixel, eval_info, sampler))
