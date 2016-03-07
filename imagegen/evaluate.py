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
from .math_help import rotate_origin


def evaluate_pixel(pixel, info, sampler):
    """
    Computes the color of a specified pixel within an image.
    :param pixel: Tuple containing the x,y coordinates of the pixel to be evaluated.
    :param info: EvalInfo object containing information about the pixel being evaluated.
    :param sampler: The Sampler implementation to be used when evaluating the pixel.
    :return: Color of the pixel at the specified coordinates.
    """
    color = Color()
    for info.x, info.y in sampler.next_sample(pixel):
        info.x, info.y = rotate_origin((info.x * info.pixel_size[0] * info.node.scaling[0],
                                        info.y * info.pixel_size[1] * info.node.scaling[1]),
                                       (0.5, 0.5),      # TODO: Retrieve origin from node
                                       info.node.rotation)
        color += info.node.evaluate(info)
    return color / len(sampler)


def evaluate_image(output, eval_info, sampler):
    """
    Computes the entire contents of an image.
    :param output: The OutputImage whose content we're evaluating.
    :param eval_info: EvalInfo object containing a description of the node being evaluated.
    :param sampler: The sampler to be used when evaluating each pixel within the image.
    """
    for pixel in output.next_pixel():
        output.set_pixel(pixel, evaluate_pixel(pixel, eval_info, sampler))
