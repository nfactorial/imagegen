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

import math

from ..color import Color
from ..math_help import smooth_step, min_max
from ..node_registry import register_node
from ..parameter import ParameterDefinition

CIRCLE_INPUT = [
    ParameterDefinition('background',
                        param_type='color',
                        default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color',
                        param_type='color',
                        default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
    ParameterDefinition('inner_radius',
                        param_type='scalar',
                        minimum=0.0,
                        maximum=1.0,
                        default_value=0.3),
    ParameterDefinition('outer_radius',
                        param_type='scalar',
                        minimum=0.0,
                        maximum=1.0,
                        default_value=0.35),
    ParameterDefinition('hardness',
                        param_type='scalar',
                        minimum=0.0,
                        maximum=1.0,
                        default_value=1.0)
]


def evaluate_circle(eval_info):
    """
    Computes the color of a circle centered in the current image.
    :param eval_info: {eval_info.py} Description of the sample being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    x, y = eval_info.x - 0.5, eval_info.y - 0.5
    distance = math.sqrt(x*x + y*y)
    inner_radius, outer_radius = min_max(eval_info.evaluate('inner_radius', eval_info.x, eval_info.y),
                                         eval_info.evaluate('outer_radius', eval_info.x, eval_info.y))
    background = eval_info.evaluate('background', eval_info.x, eval_info.y)
    if inner_radius < distance < outer_radius:
        hardness = eval_info.evaluate('hardness', eval_info.x, eval_info.y)
        distance = (distance - inner_radius) / (outer_radius - inner_radius)
        t = smooth_step(hardness, 1.0, distance) if hardness < 1.0 else 0.0
        return eval_info.evaluate('color', eval_info.x, eval_info.y).lerp(background, t)
    return eval_info.evaluate('background', eval_info.x, eval_info.y)

register_node('circle', evaluate_circle, CIRCLE_INPUT, output='color',
              description='Draws a circle with a given inner and outer radius.')
