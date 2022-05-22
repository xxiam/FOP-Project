import math
import os

class Movement():

    def createWaypoint(self,walls,limits,safe):
        '''
        self - player object
        walls - wall positions
        limits - simulation limits
        '''

        waypointList = [safe]
        wallGap = []
        for wall in walls:
            counter = 0
            temp = []
            for _ in range(limits[1]+1):
                xval = wall[0][0]
                if (xval,counter) in wall:
                    pass
                if (xval,counter) not in wall:
                    temp.append((xval + 1,counter))
                counter += 1
            wallGap.append(temp)

        hypdiff = []
        for l in wallGap:
            temp = []
            for x,y in l:
                xdiff = self.x - x
                ydiff = self.y - y
                if xdiff < 0:
                    xdiff *= -1
                    ydiff *= -1
                
                temp.append(math.hypot(xdiff,ydiff))
            hypdiff.append(temp)

        for i in range(len(walls)):
            x,y = wallGap[i][hypdiff[i].index(min(hypdiff[i]))]
            waypointList.append((x-1,y))
            waypointList.append((x,y))

        deleteWaypoints = []
        for x,y in waypointList:
            if self.x < x:
                deleteWaypoints.append((x,y))
        for i in deleteWaypoints:
            waypointList.remove(i)

        return waypointList

    def hunt(self,target):
        #passing target as lsit of player objects

        #unpack player positions
        targetPositions = []
        for player in target:
            targetPositions.append((player.x,player.y))
        
        hypdiff = []
        for x,y in targetPositions:
            xdiff = self.x - x
            ydiff = self.y - y
            if xdiff < 0: 
                xdiff *= -1
            if ydiff < 0:
                ydiff *= -1
            
            hypdiff.append(math.hypot(xdiff,ydiff))