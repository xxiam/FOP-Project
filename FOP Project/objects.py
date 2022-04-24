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

worldLimits = (100,1000)

class Human():

    def __init__(self, name):
        self.name = name
        self.y = random.randint(0, worldLimits[1] - 1)
        self.x = random.randint(0, worldLimits[0] - 1)
        self.dead = False
        self.felloff = False
        self.speed = 1

    def find(self, item, walls):
        '''
        finds the knife
        item - the location of the knives
        walls - humans cannot walk through walls like ghosts, so they have to walk around it 
        '''

        if self.felloff == True or self.dead == True:
            self.x = -10
            self.y = -10

        else:
            #how to do object avoidance (use same as practest 3 code)
            #if human is within 1 units near a wall
            
            #finding the closest knife relative to human location
            itemPos = item #[(x,y),(x,y)...]
            relativeDiff = []
            for x,y in item: #find x,y difference between human and item
                xdiff = self.x - x
                ydiff = self.y - y
                if xdiff > 0:
                    xdiff = xdiff * -1
                if ydiff > 0:
                    ydiff = ydiff * -1
                relativeDiff.append((xdiff,ydiff)) #[(x,y),(x,y)...]

            #finding closest item using pythagoras theorem
            h = []
            for i in range(len(relativeDiff)):
                hypotheuse = math.sqrt(relativeDiff[i][0] ** 2 + relativeDiff[i][1] ** 2)
                h.append(hypotheuse)

            closestItem = itemPos[h.index(min(h))] #tuple

            if self.x > closestItem[0]:
                self.x -= 1
            if self.y > closestItem[1]:
                self.y -= 1
            if self.x < closestItem[0]:
                self.x += 1 
            if self.y < closestItem[1]:
                self.y += 1
            #still need to do object avoidance

    def hunt(self, ghosts, walls):
        '''
        once the knife has been found, the humans can now hunt the ghosts, 
        ghosts will now be slower than humans but can still traverse walls

        ghosts - coordinates of ghosts as they move

        walls - humans still have to avoid walls
        '''
        pass

    def runmid(self): #movement test
        
        if self.felloff == True or self.dead == True:
            self.y = -10
            self.x = -10

        else:
            if self.x > 500:
                self.x -= self.speed

            if self.y > 500:
                self.y -= self.speed

            if self.x < 500:
                self.x += self.speed
            
            if self.y < 500:
                self.y += self.speed
            