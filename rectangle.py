from shape import Shape


class Rectangle(Shape):
    """
    A class to represent a rectangle.

    Inherits from:
        Shape: Base class for shapes.
    """

    def __init__(self, color, arm_1, arm_2):
        """
        Initialize a new Rectangle instance.

        arguments:
            color (str): The color of the rectangle.
            arm_1 (float): The length of one side.
            arm_2 (float): The length of the adjacent side.
        """
        area = arm_1 * arm_2
        perimeter = 2 * (arm_1 + arm_2)

        super().__init__(color, area, perimeter)
