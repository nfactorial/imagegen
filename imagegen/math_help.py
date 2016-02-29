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

import math


def lerp(a, b, t):
    """
    Performs a linear interpolation between two values.
    :param a: The first value in the interpolation.
    :param b: The second value in the interpolation.
    :param t: A value between 0 and 1 which defines the position of the interpolated result.
    :return: The result of the linear interpolation.
    """
    return a + (b - a) * t


def clamp(a, minimum, maximum):
    """
    Clamps the specified value to the minimum and maximum range.
    :param a: The value to be clamped.
    :param minimum: The specified minimum range.
    :param maximum: The specified maximum range.
    :return: The clamped value.
    """
    return max(minimum, min(maximum, a))


def length(x, y):
    """
    Computes the length of a two dimensional vector.
    :param x: The x coordinate of the vector.
    :param y: The y coordinate of the vector.
    :return: The length of the supplied vector.
    """
    return math.sqrt(x * x + y * y)


def smooth_step(minimum, maximum, x):
    """
    Returns a smooth hermite interpolation between 0 and 1, if a is in the range [min, max].
    Note: Based on Ken Perlin's implementation
    :param minimum: The minimum range of the x parameter.
    :param maximum: The maximum range of the x parameter.
    :param x: The specified value to be interpolated.
    :return: 0 if x is less than minimum, 1 if x is greater than maximum.
             Otherwise a value between 0 and 1.
    """
    x = clamp((x - minimum) / (maximum - minimum), 0.0, 1.0)
    return x * x * x * (x * (x * 6 - 15) + 10)


def rotate(pos, radians):
    """
    Rotates a two-dimensional vector around the origin.
    :param pos: Tuple containing the x and y coordinates of the vector to be rotated.
    :param radians: Angle (in radians) the vector is to be rotated by.
    :return: Tuple containing the rotated coordinates of the supplied position.
    """
    cos_theta, sin_theta = math.cos(radians), math.sin(radians)
    return pos[0] * cos_theta - pos[1] * sin_theta, pos[0] * sin_theta + pos[1] * cos_theta


def rotate_origin(pos, origin, radians):
    """
    Rotates a two-dimensional vector around a specified origin.
    :param pos: Tuple containing the x and y coordinates of the vector to be rotated.
    :param origin: Tuple containing the x, y coordinates of the point to be rotated around.
    :param radians: Angle (in radians) the vector is to be rotated by.
    :return: Tuple containing the rotated coordinates of the supplied position.
    """
    rot = rotate((pos[0] - origin[0], pos[1] - origin[1]), radians)
    return rot[0] + origin[0], rot[1] + origin[1]
