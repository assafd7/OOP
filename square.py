from shape import Shape


class Square(Shape):
    """
    A class to represent a square, inheriting from Shape.
    """

    def __init__(self, color, arm):
        """
        Initialize a Square with color and arm length.

        arguments:
            color (str): Color of the square.
            arm (float): Length of one side of the square.
        """
        area = arm * arm
        perimeter = arm * 4

        super().__init__(color, area, perimeter)
