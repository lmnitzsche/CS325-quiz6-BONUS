# o.py - Open Closed Principal (OCP) Example
# Objects or entities should be open for extension but closed for modification.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def initialize(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def initialize(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def initialize(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

def main():
    # Dummy values
    circle = Circle()
    circle.initialize(5)
    
    square = Square()
    square.initialize(4)
    
    rectangle = Rectangle()
    rectangle.initialize(3, 5)

    # Calculations
    print("Circle area:", circle.get_area())
    print("Square area:", square.get_area())
    print("Rectangle area:", rectangle.get_area())

if __name__ == "__main__":
    main()
