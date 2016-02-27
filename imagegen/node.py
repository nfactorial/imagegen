import math

from color import Color
from parameter import Parameter


class Node:
    """
    The node class is used to represent a single step within the generated output. Nodes may be tied together within
    the generation graph to allow for more complex image generation.
    """
    def __init__(self, parameters, output):
        """
        Prepares the node for use by the application.
        params contains the parameter values associated for the generation object contained within the node.
        method contains the generation method to be used for evaluation.
        isDirty specifies whether or not the node has been modified since it was last evaluated.
        """
        self.params = parameters
        self.output = output
        self.is_dirty = True
        self.name = None

    def evaluate(self, info):
        """
        Evaluates the contents of the node ready for use by the generation algorithm.
        """
        # TODO: Throw exception if invoked, derived class must implement this method
        pass
