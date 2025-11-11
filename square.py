def area(a):
    """
    Calculates the area of square

    Params:
    a (int) - side

    Returns area of square with side a
    """
    if a < 0:
        raise ValueError
    return a * a


def perimeter(a):
    """
    Calculates the perimeter of square

    Params:
    a (int) - side

    Returns perimeter of square with side a
    """
    if a < 0:
        raise ValueError
    return 4 * a
