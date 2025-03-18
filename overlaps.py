from circle import Circle
from vector import Vector
from rectangle import Rectangle
def point_rectangle(p: Vector, r: Rectangle):
    temp = p - r.center #finds p relative to the center of rectangle
    return abs(temp.x) < r.width/2 and abs(temp.y) < r.height/2

def point_circle(p: Vector, c: Circle):
    return (p-c.center).length() < c.radius

def rectangle_rectangle(r1: Rectangle, r2: Rectangle):
    between: Vector = r2.center - r1.center # vector between them
    if abs(between.x) > r1.width/2 + r2.width/2: return False
    if abs(between.y) > r1.height/2 + r2.height/2: return False
    return True

def circle_circle(c1: Circle, c2: Circle):
    between: Vector = c1.center - c2.center
    return between.length() < (c1.radius + c2.radius)

def rectangle_circle(r: Rectangle, c: Circle):
    clamp_x = clamp(r.center.x-r.width/2,r.center.x+r.width/2,c.center.x)
    clamp_y = clamp(r.center.y-r.height/2,r.center.y+r.height/2,c.center.y)
    return point_circle(Vector(clamp_x,clamp_y),c)

def clamp(lower: float,upper: float, value: float):
    return max(lower, min(upper, value))

if __name__=="__main__":
    print(clamp(3,7,10))
    assert rectangle_circle(Rectangle(Vector(3,4),3,7),Circle(Vector(3,9),2)) == True
    assert rectangle_circle(Rectangle(Vector(0,0),2,2),Circle(Vector(2,0),1)) == False
    assert rectangle_circle(Rectangle(Vector(0,0),2,2),Circle(Vector(1.99,0),1)) == True
    assert circle_circle(Circle(Vector(0,0),1), Circle(Vector(2,0),1)) == False
    assert circle_circle(Circle(Vector(0,0),1), Circle(Vector(1.99,0),1)) == True
    assert point_circle(Vector(0,0),Circle(Vector(0,0),1)) == True
    assert point_circle(Vector(.99999,0),Circle(Vector(0,0),1)) == True
    assert point_circle(Vector(2,2),Circle(Vector(0,0),1)) == False
    assert point_rectangle(Vector(0,0),Rectangle(Vector(0,0),1,1)) == True
    assert point_rectangle(Vector(.5,0),Rectangle(Vector(0,0),1,1)) == False