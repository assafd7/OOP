from shape import Shape


class Circle(Shape):
    """
    A class to represent a circle, inheriting from Shape.
    """

    def __init__(self, color, radius):
        """
        Initialize a Circle with color and radius.

        arguments:
            color (str): Color of the circle.
            radius (float): Radius of the circle.
        """
        area = radius ** 2 * 3.14
        perimeter = radius * 2 * 3.14

        super().__init__(color, area, perimeter)
