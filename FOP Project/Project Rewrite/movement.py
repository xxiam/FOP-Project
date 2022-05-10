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
        
        waypoint = objective[hypDiff.index(max(hypDiff))]

        #find walls first before finding objective
        try:
            if self.x < self.prevPos[0]: #moving left
                xMove = -1
            if self.x > self.prevPos[0]:
                xMove = 1
            if self.y < self.prevPos[1]: #moving down
                yMove = -1
            if self.y > self.prevPos[1]:
                yMove = 1
            self.direction = (xMove,yMove)
        except UnboundLocalError:
            pass

        for _ in range(3):
            vision = (self.x + _ * self.direction[0],self.y + _ * self.direction[1])

            if vision in wallList:
                #extrapolation of movement lands into a wall
                #find which wall and find wall location
                for k,v in walls.items():
                    if vision in v:
                        vWall = v
                        vDetails = k
                if walls[vWall].index(vision) > len(walls[vWall])/2:
                    #upper/leftside of wall
                    wallEnd = walls[vWall][-1]
                if walls[vWall].index(vision) < len(walls[vWall])/2:
                    #lower/rightside of wall
                    wallEnd = walls[vWall][0]

                if k[0] == 0:
                    if  self.x > wallEnd[0]:
                        #if pos is right of wall
                        waypoint = (wallEnd[0] + 1, wallEnd[1] + 1)
                    if self.x < wallEnd[0]:
                        waypoint = (wallEnd[0] - 1, wallEnd[1] -1)

        ##  -- do not change this -- 
        if self.x > waypoint[0]:
            self.x -= self.speed
        if self.x < waypoint[0]:
            self.x += self.speed
        if self.y > waypoint[1]:
            self.y -= self.speed
        if self.y < waypoint[1]:
            self.y += self.speed