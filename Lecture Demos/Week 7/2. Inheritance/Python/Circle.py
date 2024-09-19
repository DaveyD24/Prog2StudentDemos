from Shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(1)
    
    def area(self):
        return math.pi * self.radius * self.radius 
    
    def noCorners(self):
        return 0