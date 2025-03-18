from vector import Vector

class Rectangle:
    def __init__(self, center:Vector, width:float, height:float):
        self.center = Vector(center.x, center.y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width*2 + self.height*2
    
    def getCorners(self):
        return [
            self.center + Vector(-self.width/2, -self.height/2), #LL
            self.center + Vector(self.width/2,-self.height/2), #LR
            self.center + Vector(-self.width/2, self.height/2), #UL
            self.center + Vector(self.width/2, self.height/2), #UR
        ]
    
    def boundingCircle(self):
        from circle import Circle
        return Circle(Vector(self.center.x,self.center.y), Vector(self.width/2,self.height/2).length())
    def __str__(self):
        return f"|{self.center},w={self.width},h={self.height}|"
    
if __name__=="__main__":
    R = Rectangle(Vector(0,0),6,8)
    print(R)
    print([str(x) for x in R.getCorners()])
    print(R.area())
    print(R.perimeter())
    print(R.boundingCircle())