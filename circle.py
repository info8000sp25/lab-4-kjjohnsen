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
    def insideSquare(self):
        from rectangle import Rectangle
        # The square inside has a diagonal of 2r
        # Byte the pythagorean theorem, s^2 + s^2 = (2r)^2, so s = r*sqrt(2)
        s = self.radius*math.sqrt(2) 
        return Rectangle(self.center,s,s)
    
    def __str__(self):
        return(f"({self.center}, r={self.radius})")
    
if __name__ == "__main__":
    c = Circle(Vector(3,4),1/math.pi) #perimeter should be 2
    print(c)
    print(c.perimeter())

    c2 = Circle(Vector(3,4),1/math.sqrt(math.pi)) #area should be 1
    print(c2.area())

    c3 = Circle(Vector(0,0),1) #square sides should be 1*sqrt(2)
    print(c3.insideSquare())