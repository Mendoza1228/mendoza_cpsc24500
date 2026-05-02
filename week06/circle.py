import math
from shape import Shape

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius    
    
    def describe(self) -> str:
        return f"Circle with radius {self.radius:.1f}"


    