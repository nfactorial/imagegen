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
import noise

from ..color import Color
from ..parameter import ParameterDefinition
from ..node_registry import register_node

TURBULENCE_INPUT = [
    ParameterDefinition('octaves',
                        param_type='int',
                        default_value=1),
    ParameterDefinition('frequency',
                        param_type='scalar',
                        default_value=4.0)
]


def evaluate_turbulence(eval_info):
    """
    :param eval_info: EvalInfo object containing the sample being evaluated.
    :return: The evaluated value at the supplied sample location.
    """
    octaves = eval_info.evaluate('octaves', eval_info.x, eval_info.y)
    frequency = eval_info.evaluate('frequency', eval_info.x, eval_info.y)
    frequency_x = frequency / eval_info.image_size[0] * octaves
    frequency_y = frequency / eval_info.image_size[0] * octaves
    pnoise = noise.pnoise2(eval_info.x / frequency_x, eval_info.y / frequency_y, octaves=octaves)
    pnoise = math.fabs(pnoise)
    return Color(pnoise, pnoise, pnoise, pnoise)

register_node('turbulence', evaluate_turbulence, TURBULENCE_INPUT, output='color',
              description='Generates a random, positive 2D noise value.')
