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

from ..color import Color
from ..parameter import ParameterDefinition
from ..node_registry import register_node

MULTIPLY_INPUT = [
    ParameterDefinition('a',
                        param_type='color',
                        default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('b',
                        param_type='color',
                        default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
]


def evaluate_multiply(eval_info):
    """
    Multiplies two color values together and returns the result.
    :param eval_info: Parameters describing the sample currently being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    color_a = eval_info.evaluate('color_a', eval_info.x, eval_info.y)
    color_b = eval_info.evaluate('color_b', eval_info.x, eval_info.y)
    return Color(red=color_a.red * color_b.red,
                 green=color_a.green * color_b.green,
                 blue=color_a.blue * color_b.blue,
                 alpha=color_a.alpha * color_b.alpha)

register_node('multiply', evaluate_multiply, MULTIPLY_INPUT, output='color',
              description='Multiplies two color values together.')
