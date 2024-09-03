class Shape:
    """
    a class to represent a shape of any kind

    members:
        color (str) : color of the shape
        area (float) : the area of the shape
        perimeter (float) : the perimeter of the shape
    """
    def __init__(self, color, area, prm):
        """
        initialize a new shape

        arguments:
            color (str): The color of the shape.
            area (float): The area of the shape.
            prm (float): The perimeter of the shape.
        """
        self.color = color
        self.area = area
        self.perimeter = prm

    def set_color(self, color):
        """
        a method to set the color of the shape
            :param color:
        """
        self.color = color

    def get_color(self):
        """
        a method to get the color of the shape
        :return: (str) color of the shape
        """
        return self.color

    def get_area(self):
        """
        a method to get the area of the shape
            :return: (float) area of the shape
        """
        return self.area

    def get_perimeter(self):
        """
        a method to get the perimeter of the shape
            :return: (float) the perimeter of the shape
        """
        return self.perimeter
