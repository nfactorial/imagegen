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


def clamp(a, minval, maxval):
    """
    Clamps the specified value to the minimum and maximum range.
    :param a: The value to be clamped.
    :param minval: The specified minimum range.
    :param maxval: The specified maximum range.
    :return: The clamped value.
    """
    return max(minval, min(maxval, a))


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
    :return: 0 if x is less than minimum, 1 if x is greater than maximum. Otherwise a value between 0 and 1.
    """
    x = clamp((x - minimum) / (maximum - minimum), 0.0, 1.0)
    return x * x * x * (x * (x * 6 - 15) + 10)
