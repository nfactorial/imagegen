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


def rotate(pos, radians):
    """
    Rotates a two-dimensional vector around the origin.
    :param pos: Tuple containing the x and y coordinates of the vector to be rotated.
    :param radians: Angle (in radians) the vector is to be rotated by.
    :return: Tuple containing the rotated coordinates of the supplied position.
    """
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
    return pos[0] * cos_theta - pos[1] * sin_theta, pos[0] * sin_theta + pos[1] * cos_theta


def rotate_origin(pos, origin, radians):
    """
    Rotates a two-dimensional vector around a specified origin.
    :param pos: Tuple containing the x and y coordinates of the vector to be rotated.
    :param origin: Tuple containing the x and y coordinates of the point to be rotated around.
    :param radians: Angle (in radians) the vector is to be rotated by.
    :return: Tuple containing the rotated coordinates of the supplied position around the supplied origin.
    """
    rot = rotate((pos[0] - origin[0], pos[1] - origin[1]), radians)
    return rot[0] + origin[0], rot[1] + origin[1]
