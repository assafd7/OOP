from shape import Shape
from rectangle import Rectangle
from shapes_garage import ShapesGarage


def hibur(rec1, rec2):
    """
    Combine two rectangles into a new Shape with combined area and perimeter.

    Args:
        rec1 (Rectangle): The first rectangle.
        rec2 (Rectangle): The second rectangle.

    Returns:
        Shape: A new Shape object with combined area and perimeter of the two rectangles.
    """
    assert isinstance(rec1, Rectangle), "First argument must be a Rectangle."
    assert isinstance(rec2, Rectangle), "Second argument must be a Rectangle."

    new_rec_area = rec1.get_area() + rec2.get_area()
    new_rec_prm = rec1.get_perimeter() + rec2.get_perimeter()
    return Shape(None, new_rec_area, new_rec_prm)


def main():
    """
    Main function to create a ShapesGarage instance, generate shapes, and print summary.
    """
    my_container = ShapesGarage()
    my_container.generate(100)
    print("Total area:", my_container.sumAreas())
    print("Total perimeter:", my_container.sumPerimeter())
    print("Colors:", my_container.countColors())


if __name__ == "__main__":
    main()
