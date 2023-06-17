class Horse:
    def __init__(self,name,breed,color,speed):
        self.name=name
        self.breed=breed
        self.color=color
        self.speed=speed
class Rider:
    def __init__(self,name,horse):
        self.name=name
        self.horse=horse
#horse1=Horse("Britt","hz","brown","78")
rd1=Rider("Susan",Horse("Britt","hz","brown","78"))
print(rd1.horse.speed)