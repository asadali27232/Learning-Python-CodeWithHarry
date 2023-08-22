class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        print("Area of the shape is:")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        super().area()
        print(3.14 * self.radius**2)
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        super().area()
        print(self.side**2)
        return self.side**2


circle = Circle("Red", 4)
circle.area()
square = Square("Blue", 5)
square.area()
