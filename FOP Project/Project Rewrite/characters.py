import random
class Human():
    def __init__(self,limits,name):
        self.name = name
        self.x = random.randint(1,limits[0])
        self.y = random.randint(1,limits[1])
        self.direction = (0,0)
        self.speed = 1
        self.prevPos = (self.x,self.y)
        self.moving = True #either dead or fallen off the map

class Ghost():
    def __init__(self,limits):
        self.x = random.randint(1,limits[0])
        self.y = random.randint(1,limits[1])
        self.speed = 2
        self.moving = True