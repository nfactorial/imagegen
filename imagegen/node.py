import math

from parameter import Parameter


class Node:
    """
    The node class is used to represent a single step within the generated output. Nodes may be tied together within
    the generation graph to allow for more complex image generation.
    """
    def __init__(self, parameters):
        """
        Prepares the node for use by the application.
        params contains the parameter values associated for the generation object contained within the node.
        method contains the generation method to be used for evaluation.
        isDirty specifies whether or not the node has been modified since it was last evaluated.
        """
        self.input_pins = {}
        self.output_pins = {}
        self.method = None
        self.is_dirty = True
        self.params = {}
        self.name = desc['name']

    def evaluate(self, info):
        """
        Evaluates the contents of the node ready for use by the generation algorithm.
        """
        # TODO: Actually perform the evaluation here (or generate the tasks)
        if self.method is not None:
            self.method()
        self.is_dirty = False


checkerboard_params = {
    "color_a": Parameter(param_type="color"),
    "color_b": Parameter(param_type="color")
}


class CheckerboardNode(Node):
    def __init__(self):
        Node.__init__(self, checkerboard_params)

    def evaluate(self, info):
        x, y = math.fmod(info.pos[0], 1.0), math.fmod(info.pos[1], 1.0)
        if x < 0.5:
            if y > 0.5:
                return self.params["color_b"].evaluate(info)
        else:
            if y < 0.5:
                return self.params["color_b"].evaluate(info)
        return self.params["color_a"].evaluate(info)


circle_params = {
    "background": Parameter(param_type="color"),
    "color": Parameter(param_type="color"),
    "inner_radius": Parameter(param_type="float"),
    "outer_radius": Parameter(param_type="float")
}


class CircleNode(Node):
    def __init__(self):
        Node.__init__(self, circle_params)

    def evaluate(self, info):
        x, y = info.pos[0] - 0.5, info.pos[1] - 0.5
        d = math.sqrt(x*x + y*y)
        if self.params["inner_radius"].evaluate(info) < d < self.params["outer_radius"].evaluate(info):
            return self.params["color"].evaluate(info)
        return self.params["background"].evaluate(info)
