from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.141592653589793 * self.radius

# Example usage:
shapes = [Rectangle(10, 20), Circle(15)]

for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
