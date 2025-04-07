from Rectangle import Rectangle
from Circle import Circle
from Shape import Shape

if __name__ == "__main__":
    shapes = [Rectangle(4,5), Circle(4)]
    for s in shapes:
        print(f"Area of my {s.__class__.__name__}: {s.area():.2f}")
        print(f"Number of corners of my {s.__class__.__name__}: {s.noCorners()}")