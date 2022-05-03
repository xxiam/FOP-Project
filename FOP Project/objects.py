'''
objects.py - hunters and hunted classes

ghost class:
at the start of the simulation, the ghosts are hunting the humans,
once the humans find the holy knife, humans can now hunt ghosts,
ghosts can travel through walls and move faster than humans

humans class:
ghost prey, hunted by ghosts until they find the holy knife,
cannot travel through walls and move slower than ghosts,

'''

import random
import math

#easier moving
UP = lambda x : x + 1
DOWN = lambda x : x - 1
LEFT = UP # + x is the same as + y ( + 1 )
RIGHT = DOWN # - x is the same as - y ( - 1 )

class Human():

    def __init__(self, name, worldLimits):
        self.name = name
        self.y = random.randint(0, worldLimits[1] - 1)
        self.x = random.randint(0, worldLimits[0] - 1)
        self.dead = False
        self.felloff = False
        self.speed = 1
        self.prevPos = (self.x,self.y)
        self.avoiding = False
        self.direction = 0
        self.visionRange = 5

class Movement():
    
    def find(self,item,walls):
        itemPos = item
        wallPos = []

        for k,v in walls.items():
            wallEnd = walls[k].pop(1) #removes and returns the end of wall
            v.append(wallEnd) #appends wall ending to the end of the list of wall pos
            for _ in v:
                wallPos.append(_)
        relativeDiff = []
        hypDiff = []
            
        for x,y in itemPos:
            xdiff = self.x - x
            ydiff = self.y - y
            if xdiff < 0:
                xdiff = xdiff * -1
            if ydiff < 0:
                xdiff = xdiff * -1
            relativeDiff.append((xdiff,ydiff))

        for x,y in relativeDiff:
            if x == 0 or y == 0:
                hypDiff.append(min(relativeDiff[relativeDiff.index((x,y))]))
            else:
                hypDiff.append(math.hypot(x,y))
        closest_item = itemPos[hypDiff.index(min(hypDiff))]

        if self.felloff == True or self.dead == True:
            self.x = -10
            self.y = -10
        
        else:
            if self.prevPos[0] > self.x:
                xMove = -1
            if self.prevPos[0] < self.x:
                xMove = 1
            if self.prevPos[1] > self.y:
                yMove = -1
            if self.prevPos[1] < self.y:
                yMove = 1
            if self.prevPos[0] == self.x:
                xMove = 0
            if self.prevPos[1] == self.y:
                yMove = 0

            self.direction = (xMove,yMove)

            visionX,visionY = self.direction

            for _ in range(self.visionRange):
                visionX += self.direction[0]
                visionY += self.direction[1]
                vision = (visionX,visionY)

                if vision in wallPos:
                    self.avoiding = True
                    #finding which wall and orientation to move to that point
                    for k,v in walls.items():
                        if vision in v:
                            wallOrientation = k[0]
                            if v.index(vision) > len(v)/2: #upper half/right side
                                if wallOrientation == 0:
                                    if self.x > v[-1][0]:
                                        waypoint = (v[-1][0] +1, v[-1][1] + 1)
                                    if self.x < v[-1][0]:
                                        waypoint = (v[-1][0] -1, v[-1][1] + 1)
                                wallEdge = v[-1]

                            if v.index(vision) < len(v)/2: #lower half/left side
                                if wallOrientation == 0:
                                    if self.x > v[0][0]:
                                        waypoint = (v[0][0] + 1, v[0][1] - 1)
                                    if self.x < v[0][0]:
                                        waypoint = (v[0][0] - 1, v[0][1] - 1)
                                wallEdge = v[0]
                else:
                    pass                    
                   

        if self.avoiding == False:
            if self.x > closest_item[0]:
                self.x = RIGHT(self.x)
            if self.x < closest_item[0]:
                self.x = LEFT(self.x)
            if self.y > closest_item[1]:
                self.y = DOWN(self.y)
            if self.y < closest_item[1]:
               self.x = UP(self.y)
            
        if self.avoiding == True:
            pass