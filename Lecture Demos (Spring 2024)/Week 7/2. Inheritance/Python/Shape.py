from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, noSides):
        self.noSides = noSides
    
    @abstractmethod
    def area(self):
        pass

    def noCorners(self):
        return self.noSides