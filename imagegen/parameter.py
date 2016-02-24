import math


class Parameter:
    def __init__(self):
        self.name = ""
        self.display_name = ""
        self.param_type = "int"
        self.minimum = math.inf
        self.has_minimum = False
        self.maximum = -math.inf
        self.has_maximum = False

    def has_range(self):
        """
        Determines whether or not this parameter contains a valid range limit.
        """
        return self.has_minimum and self.has_maximum
