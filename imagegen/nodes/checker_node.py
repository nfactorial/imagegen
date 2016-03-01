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
from ..parameter import ParameterDefinition
from ..node_registry import register_node

CHECKERBOARD_INPUT = [
    ParameterDefinition('color_a',
                        param_type='color',
                        default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color_b',
                        param_type='color',
                        default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0))
]

CHECKERBOARD_GPU_PROGRAM = 'vec4 evaluate_checkerboard(vec4 color_a, vec4 color_b) {'   \
                           '}'


def evaluate_checkerboard(eval_info):
    """
    Computes the color of a sample within a checker pattern.
    :param eval_info: Parameters describing the sample currently being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    x = math.fmod(eval_info.x if eval_info.x >= 0.0 else math.fabs(eval_info.x - 0.5), 1.0)
    y = math.fmod(eval_info.y if eval_info.y >= 0.0 else math.fabs(eval_info.y - 0.5), 1.0)
    if x < 0.5:
        if y > 0.5:
            return eval_info.evaluate('color_b', x / 0.5, (y - 0.5) / 0.5)
        return eval_info.evaluate('color_a', x / 0.5, y / 0.5)

    if y < 0.5:
        return eval_info.evaluate('color_b', (x - 0.5) / 0.5, y / 0.5)
    return eval_info.evaluate('color_a', (x - 0.5) / 0.5, (y - 0.5) / 0.5)

register_node('checker', evaluate_checkerboard, CHECKERBOARD_INPUT, output='color',
              gpu_program=CHECKERBOARD_GPU_PROGRAM,
              description='Creates a pattern of squares using two colors.')
