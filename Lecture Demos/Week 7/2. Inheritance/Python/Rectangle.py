from Shape import Shape

class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(4)
        self.height = height
        self.width = width
    
    def area(self):
        return self.height * self.width