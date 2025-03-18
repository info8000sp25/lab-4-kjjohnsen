from vector import Vector
import math
class Circle:
    def __init__(self, center:Vector, radius:float):
        self.center = Vector(center.x,center.y) # good idea to copy it, instead of just assigning
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius
    def __str__(self):
        return(f"({self.center}, r={self.radius})")
    
if __name__ == "__main__":
    c = Circle(Vector(3,4),1/math.pi) #perimeter should be 2
    print(c)
    print(c.perimeter())

    c2 = Circle(Vector(3,4),1/math.sqrt(math.pi)) #area should be 1
    print(c2.area())