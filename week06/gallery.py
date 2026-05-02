from shape import Shape


class Gallery:
    def __init__(self, name: str):
        self.name = name
        self.shapes = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)
    
    def largest_shape(self):
        if not self.shapes:
            return None
        return max(self.shapes, key=lambda shape: shape.area()) 
    
    def display_all(self):
        print(f"\n--- {self.name} Gallery ---")
        print(f"Number of shapes: {len(self.shapes)}")
        for i, shape in enumerate(self.shapes, start=1):
            print(f"{i}. {shape.describe()} - Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
        print("-------------------------\n ")
