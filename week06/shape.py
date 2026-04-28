from abc import ABC, abstractmethod


class Shape(ABC):
    # Abstract base class for shapes
    @abstractmethod
    def area(self) -> float:
        pass
    # Each subclass must implement the area method to calculate the area of the shap
    @abstractmethod
    def perimeter(self) -> float:
        pass
    # Each subclass must implement the perimeter method to calculate the perimeter of the shape
    @abstractmethod
    def describe(self) -> str:
        pass

