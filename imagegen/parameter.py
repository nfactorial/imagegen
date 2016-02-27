import math


class ParameterDefinition:
    """
    Describes a parameter that is exposed within the application.
    Parameters are values that may be edited by the user, they may also be connected to the output
    of a node that computes a compatible value.
    The ParameterDefinition class is used to describe a parameter, however the Parameter class itself
    is used to represent an actual instance of a parameter.
    """
    def __init__(self, name, param_type=None, minimum=None, maximum=None, default_value=None):
        self.name = name
        self.param_type = param_type
        self.minimum = math.inf if minimum is None else minimum
        self.has_minimum = False if minimum is None else True
        self.maximum = -math.inf if maximum is None else maximum
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
