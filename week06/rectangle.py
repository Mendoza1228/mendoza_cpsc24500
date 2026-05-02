from shape import Shape


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def describe(self) -> str:
        return f"Rectangle with width {self.width:.1f} and height {self.height:.1f}"
    
        
