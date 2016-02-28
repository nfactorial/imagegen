"""
Copyright 2016 nfactorial

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .math_help import lerp


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

    def lerp(self, other, t):
        """
        Performs a linear interpolation between two colors.
        :param other: The second color for the interpolation operation.
        :param t: A value between 0 and 1. Where 0 will return the first color and 1 will return the second. Any
                  value between this range will result in a blend between the two.
        :return: The interpolated color.
        """
        return Color(lerp(self.red, other.red, t),
                     lerp(self.green, other.green, t),
                     lerp(self.blue, other.blue, t),
                     lerp(self.alpha, other.alpha, t))
