import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return  (math.pi * self.radius * self.radius)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length * self.length
    

def print_area(shape_object):
    print(shape_object.area())

c1 = Circle(4)
s1 = Square(5)
print_area(c1)
print_area(s1)

    
       