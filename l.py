# l.py - Liskov Substitution Principle (LSP) Example
# Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T.
# objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. 
# In other words, a subtype should be substitutable for its base type.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def set_width(self, width):
        self.radius = width

    def set_height(self, height):
        self.radius = height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.length = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

    def set_width(self, width):
        self.base = width

    def set_height(self, height):
        self.height = height

class Polygon(Shape):
    def __init__(self, num_sides, side_length):
        self.num_sides = num_sides
        self.side_length = side_length

    def get_area(self):
        return 0.25 * self.num_sides * self.side_length ** 2 * (1 / math.tan(math.pi / self.num_sides))

    def set_width(self, width):
        self.side_length = width

    def set_height(self, height):
        self.side_length = height

def main():
    # Dummy values
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 5)
    triangle = Triangle(4, 6)
    polygon = Polygon(6, 7)

    # Calculate and output areas
    print("Circle area:", circle.get_area())
    print("Square area:", square.get_area())
    print("Rectangle area:", rectangle.get_area())
    print("Triangle area:", triangle.get_area())
    print("Polygon area:", polygon.get_area())

if __name__ == "__main__":
    main()
