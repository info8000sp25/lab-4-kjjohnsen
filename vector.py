import math
class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
    def __str__(self):
        return f"<{self.x}, {self.y}>"
    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x, self.y-other.y)
    
if __name__=="__main__":
    print(Vector(3,4))
    print(Vector(2,3)+Vector(3,4))
    print(Vector(2,3)-Vector(3,5))
    print(Vector(3,4).length())