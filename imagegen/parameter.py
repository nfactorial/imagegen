import math


def read_scalar_json(param, desc):
    """
    Reads the scalar parameter value from the supplied json data.
    :param param: The parameter whose value is being read.
    :param desc: Json description of the parameter.
    """
    if 'value' in desc:
        param.current_value = desc['value']
    else:
        param.current_value = param.definition.default_value


def read_color_json(param, desc):
    """
    Reads the color parameter value from the supplied json data.
    :param param: The parameter whose value is being read.
    :param desc: Json description of the parameter.
    """
    param.current_value = (desc['rgb'][0], desc['rgb'][1], desc['rgb'][2])


# This dictionary maps the parsing function to the parameter types
json_param_readers = {
    'scalar': read_scalar_json,
    'color': read_color_json
}


class ParameterDefinition:
    """
    Describes a parameter that is exposed within the application.
    Parameters are values that may be edited by the user, they may also be connected to the output
    of a node that computes a compatible value.
    The ParameterDefinition class is used to describe a parameter, however the Parameter class itself
    is used to represent an actual instance of a parameter.
    """
    def __init__(self, name, param_type=None, minimum=None, maximum=None, default_value=None):
        if param_type not in json_param_readers:
            raise TypeError
        self.read_json = json_param_readers[param_type]
        self.name = name
        self.param_type = param_type
        self.minimum = float('Inf') if minimum is None else minimum
        self.has_minimum = False if minimum is None else True
        self.maximum = -float('Inf') if maximum is None else maximum
        self.has_maximum = False if maximum is None else True
        self.default_value = default_value
        self.node = None

    @property
    def has_range(self):
        """
        Determines whether or not this parameter contains a valid range limit.
        """
        return self.has_minimum and self.has_maximum


class Parameter:
    """
    Represents an instance of a Parameter within the application.
    A parameter may be bound to a node as long as the nodes output type matches the parameter type.
    If a parameter has been bound, its 'binding' property will contain a reference to the node it
    has been bound to.
    """
    def __init__(self, definition):
        """
        Creates an instance of a parameter described by the supplied ParameterDefinition object.
        :param definition: ParameterDefinition that describes the parameter being represented.
        """
        self.definition = definition
        self.current_value = definition.default_value
        self.binding = None

    @property
    def minimum(self):
        """
        Retrieves the minimum value this parameter may be assigned.
        :return: The minimum value that may be assigned to the parameter.
        """
        return self.definition.minimum

    @property
    def maximum(self):
        """
        Retrieves the maximum value this parameter may be assigned.
        :return: The maximum value that may be assigned to the parameter.
        """
        return self.definition.maximum

    @property
    def has_range(self):
        """
        Determines whether or not this parameter has a valid range setting.
        :return: True if the parameter has a valid range otherwise False.
        """
        return self.definition.has_range

    @property
    def name(self):
        """
        Retrieves the name associated with the parameter.
        :return: The name of the parameter.
        """
        return self.definition.name

    def read_json(self, desc):
        """
        Reads the contents of the parameter from the supplied json data.
        :param desc: Json description of the parameter.
        """
        if 'bind' in desc:
            self.binding = desc['bind']
        else:
            self.definition.read_json(self, desc)

    def bind(self, node):
        """
        Binds the parameters value to the output of a specified node.
        :param node: The node to which the parameter will be bound.
        """
        if node is None:
            raise TypeError
        if node.output != self.definition.param_type:
            raise TypeError
        self.binding = node
