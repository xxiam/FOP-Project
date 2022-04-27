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

    def find(self, item, walls):
        '''
        finds the knife
        item - the location of the knives
        walls - humans cannot walk through walls like ghosts, so they have to walk around it 
        '''
        itemPos = item
        wallDetails = []
        wallPos = []

        for k,v in walls.items():
            wallEnd = walls[k].pop(1)
            v.append(wallEnd)
            wallDetails.append(k)
            for _ in v:
                wallPos.append(_)

        if self.felloff == True or self.dead == True:
            self.x = -10
            self.y = -10

        else:
            #finds the nearest item
            relativeDiff = []
            hypDiff = []
            for x,y in itemPos:
                xdiff = self.x - x
                ydiff = self.y - y
                if xdiff < 0:
                    xdiff = xdiff * -1
                if ydiff < 0:
                    ydiff = ydiff * -1
                relativeDiff.append((xdiff,ydiff))

            for x,y in relativeDiff:
                hypothenuse = math.sqrt(x ** 2 + y ** 2)
                hypDiff.append(hypothenuse)

            closestItem = itemPos[hypDiff.index(min(hypDiff))]
            if self.avoiding == False:
                if self.x > closestItem[0]:
                    self.x -= self.speed
                if self.x < closestItem[0]:
                    self.x += self.speed
                if self.y > closestItem[1]:
                    self.y -= self.speed
                if self.y < closestItem[1]:
                    self.y += self.speed
            #object avoidance
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

            visionRange = 10
            direction = (xMove,yMove) #-1 = moving -x/y, 1 = moving +x/y

            xVision = self.x
            yVision = self.y

            for v in range(visionRange):
                if direction[0] == 1:
                    xVision += 1
                if direction[0] == -1:
                    xVision -= 1
                if direction[1] == 1:
                    yVision += 1
                if direction[1] == -1:
                    yVision -= 1
                vision = (xVision,yVision)
                 
                if vision in wallPos:
                    self.avoiding = True
                    #find which wall the human is facing and the orientation
                    facingWall = wallDetails[wallPos.index(vision)]
                    #facingWall = (orientation, wallNumber)
                    wallList = wallPos[facingWall[1]]

                    if wallList.index(vision) > len(wallList): #second half
                        wallEdge = wallList[-1]
                    if wallList.index(vision) < len(wallList): #first half
                        wallEdge = wallList[0]

            if self.avoiding == True:
                pass        
                #wallEdge is a tuple of the edge of the wall
                #create movement system to move to the edge of the wall
                #once finished, return to normal find method
                    #move to wallEdge
                    
    def hunt(self, ghosts, walls):
        '''
        once the knife has been found, the humans can now hunt the ghosts, 
        ghosts will now be slower than humans but can still traverse walls

        ghosts - coordinates of ghosts as they move

        walls - humans still have to avoid walls
        '''
        self.speed = 2

class Ghost():
    
    def __init__(self,worldLimits):
        self.y = random.randint(0,worldLimits[1] -1 )
        self.x = random.randint(0,worldLimits[0])
        self.dead = False
        self.felloff = False
        self.speed = 2
        self.prevPos = (self.x,self.y)

    