class Color:
    """
    This class represents a four component color value with red, green, blue and alpha channels.
    """
    def __init__(self, red=0.0, green=0.0, blue=0.0, alpha=1.0):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __add__(self, other):
        self.red += other.red
        self.green += other.green
        self.blue += other.blue
        self.alpha += other.alpha
        return self

    def __mul__(self, other):
        self.red *= other
        self.green *= other
        self.blue *= other
        self.alpha *= other
        return self

    def __div__(self, other):
        self.red /= other
        self.green /= other
        self.blue /= other
        self.alpha /= other
        return self

    def __truediv__(self, other):
        self.red /= other
        self.green /= other
        self.blue /= other
        self.alpha /= other
        return self
