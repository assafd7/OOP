from rectangle import Rectangle
from square import Square
from circle import Circle
import random

COLORS_LIST = ['pink', 'red', 'blue', 'yellow', 'purple']
SHAPES = ['rectangle', 'square', 'circle']


class ShapesGarage:
    """
    A class to manage and analyze a collection of randomly generated shapes.
    """

    def __init__(self):
        """
        Initialize a ShapesGarage instance.
        """
        self.sum_areas = 0
        self.sum_prms = 0
        self.colors_dict = {color: 0 for color in COLORS_LIST}

    def generate(self, x):
        """
        Generate `x` random shapes and update area, perimeter, and color counts.

        Args:
            x (int): The number of shapes to generate.
        """
        for _ in range(x):
            color = random.choice(COLORS_LIST)
            self.colors_dict[color] += 1
            shape_type = random.choice(SHAPES)

            if shape_type == 'rectangle':
                arm1_len = random.randint(1, 10)
                arm2_len = random.randint(1, 10)
                rec = Rectangle(color, arm1_len, arm2_len)
                assert rec.get_area() == arm1_len * arm2_len, "Rectangle area is incorrect."
                assert rec.get_perimeter() == 2 * (arm1_len + arm2_len), "Rectangle perimeter is incorrect."
                self.sum_areas += rec.get_area()
                self.sum_prms += rec.get_perimeter()

            elif shape_type == 'square':
                arm_len = random.randint(1, 10)
                sqr = Square(color, arm_len)
                assert sqr.get_area() == arm_len * arm_len, "Square area is incorrect."
                assert sqr.get_perimeter() == arm_len * 4, "Square perimeter is incorrect."
                self.sum_areas += sqr.get_area()
                self.sum_prms += sqr.get_perimeter()

            elif shape_type == 'circle':
                radius = random.randint(1, 10)
                crcl = Circle(color, radius)
                assert crcl.get_area() == radius ** 2 * 3.14, "Circle area is incorrect."
                assert crcl.get_perimeter() == radius * 2 * 3.14, "Circle perimeter is incorrect."
                self.sum_areas += crcl.get_area()
                self.sum_prms += crcl.get_perimeter()

    def sumAreas(self):
        """
        Get the total area of all generated shapes.

        Returns:
            float: The total area.
        """
        return self.sum_areas

    def sumPerimeter(self):
        """
        Get the total perimeter of all generated shapes.

        Returns:
            float: The total perimeter.
        """
        return self.sum_prms

    def countColors(self):
        """
        Get the count of each color used in the generated shapes.

        Returns:
            dict: A dictionary with color counts.
        """
        return self.colors_dict
