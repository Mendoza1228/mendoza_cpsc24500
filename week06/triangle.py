import math
from shape import Shape

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be positive numbers.")
        
        # Check if the sides can form a triangle
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("The given sides do not form a triangle.")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c        

    def area(self) -> float:
        # Using Heron's formula to calculate the area of the triangle
        s = (self.side_a + self.side_b + self.side_c) / 2  # Semi-perimeter
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))     
    
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
    
    def describe(self) -> str:
        return f"Triangle with sides {self.side_a:.1f}, {self.side_b:.1f}, {self.side_c:.1f}"
    
    