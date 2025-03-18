# I am a graphics person, so this class represents the concept of a line, which is multiple points
# I added one simple function to calculate the length of the line

from vector import Vector
class Line:
    def __init__(self,points:list[Vector]):
        self.id = id
        self.points = points
    def __str__(self):
        return ", ".join([str(x) for x in self.points])
    def length(self):
        if len(self.points) < 2: return 0
        return sum([(x1-x2).length() for x1,x2 in zip(self.points[:-1],self.points[1:])])

if __name__=="__main__":
    l = Line([Vector(0,0),Vector(1,0),Vector(1,1),Vector(0,1),Vector(0,0)])
    print(l)
    print(l.length())