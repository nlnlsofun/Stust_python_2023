import math

class GeometryCalculator:
    def __init__(self, square_side=None, length=None, width=None, radius=None):
        self.square_side = square_side
        self.length = length
        self.width = width
        self.radius = radius

    def getSquareArea(self):
        if self.square_side is not None:
            return self.square_side ** 2
        else:
            return None 

    def getRectangleArea(self):
        if self.length is not None and self.width is not None:
            return self.length * self.width
        else:
            return None 

    def getCircleArea(self):
        if self.radius is not None:
            return math.pi * self.radius ** 2
        else:
            return None  
calculator = GeometryCalculator(square_side=5, length=6, width=8, radius=3)

# 求各種面積
square_area = calculator.getSquareArea()
rectangle_area = calculator.getRectangleArea()
circle_area = calculator.getCircleArea()

# 印出結果
print(f"Square Area: {square_area}")
print(f"Rectangle Area: {rectangle_area}")
print(f"Circle Area: {circle_area}")


 


