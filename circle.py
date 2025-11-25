import math


def area(r):
    """
    Calculates the area of circle

    Params:
    r (int) - radius

    Returns area of circle with radius a
    """
    if r < 0:
        raise ValueError
    return math.pi * r * r


def perimeter(r):
    """
    Calculates the perimeter of circle

    Params:
    r (int) - radius

    Returns perimeter of circle with radius a
    """
    if r < 0:
        raise ValueError
    return 2 * math.pi * r
