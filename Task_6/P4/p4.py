class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return (self.length * self.width)
    
rec = Rectangle(3,5)
print(f"The area of the rectangle is {rec.get_area()}")