# solution cell

from math import pi
from typing import Optional


class AreaCalculator:
    
    
    def __init__(self, radius: int):
        self.radius = radius
    def area(self) -> Optional[float]:
        if (self.radius is not None) and (self.radius > 0):
            my_area: float = (self.radius ** 2) * pi
            return my_area
        return None
