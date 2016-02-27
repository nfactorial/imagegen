from imagegen.math_help import rotate_origin


class EvalInfo:
    """
    Contains the properties necessary for a node to evaluate its result for a particular sample.
    The intent of the EvalInfo object is to supply an evaluation function with the data necessary
    for computing its resulting value, abstracting away the complexity of how the parameters are
    actually computed.
    The EvalInfo object contains the x,y coordinates of the sample being evaluated.
    """
    def __init__(self, node):
        if node is None:
            raise TypeError
        self.node = node
        self.x = 0.0
        self.y = 0.0

    @property
    def pos(self):
        """
        Returns the x and y position being evaluated as a tuple.
        :return: The x and y position being evaluated, as a tuple.
        """
        return self.x, self.y

    def evaluate(self, name, x, y):
        """
        Evaluates the value of a parameter at the specified sample position.
        :param name: Name of the parameter to be evaluated.
        :param x: Position of the sample to be evaluated along the horizontal axis.
        :param y: Position of the sample to be evaluated along the vertical axis.
        :return: The computed result of the parameter.
        """
        p = self.node.params[name]
        if p.binding:
            info = EvalInfo(p.binding)
            info.x, info.y = rotate_origin((x * p.binding.scale[0], y * p.binding.scale[1]), p.binding.scale, p.binding.rotation)
            return p.binding.evaluate(info)
        return p.default_value
