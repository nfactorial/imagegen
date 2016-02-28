import math

from imagegen.color import Color
from imagegen.node_registry import register_node
from imagegen.parameter import ParameterDefinition

circle_input = [
    ParameterDefinition('background', param_type='color', default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    ParameterDefinition('color', param_type='color', default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0)),
    ParameterDefinition('inner_radius', param_type='scalar', minimum=0.0, maximum=1.0, default_value=0.3),
    ParameterDefinition('outer_radius', param_type='scalar', minimum=0.0, maximum=1.0, default_value=0.35)
]


def evaluate_circle(eval_info):
    """
    Computes the color of a circle centered in the current image.
    :param eval_info: Parameters describing the sample currently being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    x, y = eval_info.x - 0.5, eval_info.y - 0.5
    d = math.sqrt(x*x + y*y)
    inner_radius = eval_info.evaluate('inner_radius', eval_info.x, eval_info.y)
    outer_radius = eval_info.evaluate('outer_radius', eval_info.x, eval_info.y)
    if inner_radius < d < outer_radius:
        return eval_info.evaluate('color', eval_info.x, eval_info.y)
    return eval_info.evaluate('background', eval_info.x, eval_info.y)

register_node('imagegen.circle', evaluate_circle, circle_input, output='color')
