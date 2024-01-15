# Polymorphism in Python

# Polymorphism is a key concept in object-oriented programming (OOP). It allows objects of different classes to be treated as objects of a common superclass. Here's an example:

# Define a base class called "Shape"
class Shape:
    def area(self):
        pass  # Placeholder for the area method

# Define derived classes: "Rectangle" and "Circle"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159265359 * self.radius * self.radius

# Create instances of the derived classes
rectangle1 = Rectangle(5, 4)
circle1 = Circle(3)

# Calculate the area using polymorphism
shapes = [rectangle1, circle1]
for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 20
# Area: 28.274333882339
