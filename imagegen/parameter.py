import math


class Parameter:
    def __init__(self, param_type=None, minimum=None, maximum=None):
        self.name = None
        self.param_type = param_type
        self.minimum = math.inf if minimum is None else minimum
        self.has_minimum = False if minimum is None else True
        self.maximum = -math.inf if maximum is None else maximum
        self.has_maximum = False if maximum is None else True

    @property
    def has_range(self):
        """
        Determines whether or not this parameter contains a valid range limit.
        """
        return self.has_minimum and self.has_maximum
