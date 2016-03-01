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

BLEND_INPUT = [
    ParameterDefinition('color_a',
                        param_type='color',
                        default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color_b',
                        param_type='color',
                        default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
    ParameterDefinition('t',
                        param_type='scalar',
                        default_value=0.5)
]

BLEND_GPU_PROGRAM = 'vec4 evaluate_blend(vec4 color_a, vec4 color_b, t) {'  \
                    '    return lerp(color_a, color_b, t);'                 \
                    '}'


def evaluate_blend(eval_info):
    """
    Computes the blend of two colors given an interpolation value.
    :param eval_info: Parameters describing the sample currently being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    color_a = eval_info.evaluate('color_a', eval_info.x, eval_info.y)
    color_b = eval_info.evaluate('color_b', eval_info.x, eval_info.y)
    return color_a.lerp(color_b, eval_info.evaluate('t', eval_info.x, eval_info.y))

register_node('blend', evaluate_blend, BLEND_INPUT, output='color',
              description='Blends between two colors based on an interpolation value.')
