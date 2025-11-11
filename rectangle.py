def area(a, b):
    """
    Calculates the area of rectangle

    Params:
    a (int) - width
    b (int) - heigth

    Returns area of rectangle with width a and heigth b
    """
    if a < 0 or b < 0:
        raise ValueError
    return a * b


def perimeter(a, b):
    """
    Calculates the perimeter of rectangle

    Params:
    a (int) - width
    b (int) - heigth

    Returns perimeter of rectangle with width a and heigth b
    """
    if a < 0 or b < 0:
        raise ValueError
    return 2 * (a + b)
