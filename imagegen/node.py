class Node:
    """
    The node class is used to represent a single step within the generated output. Nodes may be tied together within
    the generation graph to allow for more complex image generation.
    """
    def __init__(self, desc):
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

    def eval(self):
        """
        Evaluates the contents of the node ready for use by the generation algorithm.
        """
        # TODO: Actually perform the evaluation here (or generate the tasks)
        if self.method is not None:
            self.method()
        self.is_dirty = False
