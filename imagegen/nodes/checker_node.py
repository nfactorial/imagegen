import math

from imagegen.color import Color
from imagegen.parameter import Parameter
from imagegen.node_registry import register_node

checkerboard_input = {
    'color_a': Parameter(param_type='color', default_value=Color(red=0.0, green=0.0, blue=0.0, alpha=1.0)),
    'color_b': Parameter(param_type='color', default_value=Color(red=1.0, green=1.0, blue=1.0, alpha=1.0))
}


def evaluate_checkerboard(eval_info):
    """
    Computes the color of a sample within a checker pattern.
    :param eval_info: Parameters describing the sample currently being evaluated.
    :return: The evaluated color at the supplied sample location.
    """
    x, y = math.fmod(eval_info.pos.x, 1.0), math.fmod(eval_info.pos.y, 1.0)
    if x < 0.5:
        if y > 0.5:
            return eval_info.evaluate('color_b', x / 0.5, (y - 0.5) / 0.5)
        return eval_info.evaluate('color_a', x / 0.5, y / 0.5)

    if y < 0.5:
        return eval_info.evaluate('color_b', (x - 0.5) / 0.5, y / 0.5)
    return eval_info.evaluate('color_a', (x - 0.5) / 0.5, (y - 0.5) / 0.5)


register_node('imagegen.checkerboard', evaluate_checkerboard, checkerboard_input, output='color')
