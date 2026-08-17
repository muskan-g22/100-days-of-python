# 88	Demonstrate method overriding using shapes.
class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def area(self):
        radius = 5
        print("Area of Circle:", 3.14 * radius * radius)


class Rectangle(Shape):
    def area(self):
        length = 10
        width = 5
        print("Area of Rectangle:", length * width)


class Triangle(Shape):
    def area(self):
        base = 10
        height = 6
        print("Area of Triangle:", 0.5 * base * height)


# Creating objects
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

circle.area()
rectangle.area()
triangle.area()