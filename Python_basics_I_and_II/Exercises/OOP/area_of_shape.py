import math 

class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w , self.h = w, h
    def area(self):
        return self.w * self.h
class Traingle(Shape):
    def __init__(self, b, h):
        self.b, self.h = b, h
    def area(self):
        return 0.5 * self.b * self.h

shapes = [Circle(5), Rectangle(6, 4), Traingle(6, 4)]

for shape in shapes:
    print(shape.area())