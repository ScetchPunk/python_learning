import math


class Circle:
    def __init__(self, rad=0):
        self.radius = rad

    def area(self):
        return math.pi * self.radius * self.radius
    
cir1=Circle(4)
print(cir1.area())
