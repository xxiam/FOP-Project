from math import hypot
import matplotlib.pyplot as plt

class MovementV2():

    def find(self,itemPos,wallDict,limits):
        #updating self.prevPos
        self.prevPos = (self.x,self.y)

        wallPos = []
        for k,v in wallDict.items():
            wallPos.append(v)
        #wall avoidance code using waypoints
        for _ in range(5):
            pass
        #item finding code using waypoints
        hyp = []

        for x,y in itemPos:
            xDiff = self.x - x
            yDiff = self.y - y

            if xDiff < 0:
                xDiff = xDiff * -1
            if yDiff < 0:
                yDiff = yDiff * -1

            hyp.append(hypot(xDiff,yDiff))

        try:
            waypoint = itemPos[hyp.index(min(hyp))]

        except ValueError:
            print('no more knives')

        if (self.x,self.y) in itemPos:
            itemPos.remove((self.x,self.y)) #also removes knife from list in main.py

        '''
        movement code using waypoints, 
        direct humans using waypoints rather than item/wall position based of vision
        '''
        if self.dead == False or self.felloff == False:
            if self.x > waypoint[0]:
                self.x -= self.speed
            if self.x < waypoint[0]:
                self.x += self.speed
            if self.y > waypoint[1]:
                self.y -= self.speed
            if self.y < waypoint[1]:
                self.y += self.speed
        else:
            pass