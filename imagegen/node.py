from parameter import Parameter


class Node:
    """
    The node class is used to represent a single step within the generated output. Nodes may be tied together within
    the generation graph to allow for more complex image generation.
    """
    def __init__(self, name, definition):
        """
        Prepares the node for use by the application.
        :param definition: The NodeDefinition which describes the node we're representing.
        """
        self.name = name
        self.rotation = 0.0
        self.origin = (0.5, 0.5)
        self.scaling = (1.0, 1.0)
        self.definition = definition
        self.evaluate = definition.evaluate
        self.params = {p.name: Parameter(p) for p in definition.input}
        self.output = definition.output

    def read_json(self, desc):
        if 'origin' in desc:
            self.origin = (desc['origin'][0], desc['origin'][1])
        else:
            self.origin = (0.0, 0.0)
        if 'scaling' in desc:
            self.scaling = (desc['scaling'][0], desc['scaling'][1])
        else:
            self.scaling = (1.0, 1.0)
        if 'params' in desc:
            for p in desc['params']:
                if p.name in self.params:
                    self.params[p.name].read_json(p)
                else:
                    print('Warn: Parameter \'' + p.name + '\' does not exist in node type \'' + self.definition.name + '\'.')
