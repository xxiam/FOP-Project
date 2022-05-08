'''
movement classes for both humans and ghosts
'''

from math import hypot

class Movement():

    def find(self,objective,walls,limits):
        '''
        objective - for humans it should be the positions of the items 
                    - for ghosts the objective should the the positions of humans
        walls - wall positions as a dictionary
        '''

        wallList = []
        for v in walls.values():
            wallList.append(v)

        #finding the closest item using pythagoras theorem
        hypDiff = []
        for x,y in objective:
            xDiff = x - self.x
            yDiff = y - self.y

            if xDiff < 0:
                xDiff = xDiff * -1
            elif yDiff < 0:
                yDiff = yDiff * -1

            if xDiff == 0 or yDiff == 0:
                hypDiff.append(min(xDiff,yDiff))

            else:
                hypDiff.append(hypot(xDiff,yDiff))
        
        waypoint = objective[hypDiff.index(min(hypDiff))]

        #find walls first before finding objective

        if self.x < self.prevPos: #moving left
            self.direction[0] = -1
        if self.x > self.prevPos:
            self.direction[0] = 1
        if self.y < self.prevPos: #moving down
            self.direction[1] = -1
        if self.y > self.prevPos:
            self.direction[1] = 1

        for _ in range(3):
            vision = (self.x + _ * self.direction[0],self.y + _ * self.direction[1])

            if vision in wallList:
                


        ##  -- do not touch -- 
        if self.x > waypoint[0]:
            self.x -= self.speed
        if self.x < waypoint[0]:
            self.x += self.speed
        if self.y > waypoint[1]:
            self.y -= self.speed
        if self.y < waypoint[1]:
            self.y += self.speed