import math
class Movement():

    def createWaypoint(self,walls,limits,safe):
        '''
        self - player object
        walls - wall positions
        limits - simulation limits
        '''
        #grab all xpos of walls
        xVal = []
        waypointList = [safe]
        wallGap = []
        wallsLeft = []

        for wall in walls:
            for x,y in wall:
                xVal.append(x)
                xSet = set(xVal)

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
        
        temp = []
        for loc in walls:
            
            print(loc)
            if loc[0][0] in xSet:
                waypointList.remove(loc)

        return waypointList
walls = [[(16, 15), (16, 16), (16, 17), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (16, 24), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31), (16, 32), (16, 33), (16, 34), (16, 35), (16, 36), (16, 37), (16, 38), (16, 39), (16, 40), (16, 41), (16, 42), (16, 43), (16, 44), (16, 45), (16, 46), (16, 47), (16, 48), (16, 49), (16, 50), (16, 0), (16, 1), (16, 2), (16, 3)], [(32, 35), (32, 36), (32, 37), (32, 38), (32, 39), (32, 40), (32, 41), (32, 42), (32, 43), (32, 44), (32, 45), (32, 46), (32, 47), (32, 48), (32, 49), (32, 50), (32, 0), (32, 1), (32, 2), (32, 3), (32, 4), (32, 5), (32, 6), (32, 7), (32, 8), (32, 9), (32, 10), (32, 11), (32, 12), (32, 13), (32, 14), (32, 15), (32, 16), (32, 17), (32, 18), (32, 19), (32, 20), (32, 21), (32, 22), (32, 23)], [(48, 3), (48, 4), (48, 5), (48, 6), (48, 7), (48, 8), (48, 9), (48, 10), (48, 11), (48, 12), (48, 13), (48, 14), (48, 15), (48, 16), (48, 17), (48, 18), (48, 19), (48, 20), (48, 21), (48, 22), (48, 23), (48, 24), (48, 25), (48, 26), (48, 27), (48, 28), (48, 29), (48, 30), (48, 31), (48, 32), (48, 33), (48, 34), (48, 35), (48, 36), (48, 37), (48, 38), (48, 39), (48, 40), (48, 41), (48, 42)], [(64, 43), (64, 44), (64, 45), (64, 46), (64, 47), (64, 48), (64, 49), (64, 50), (64, 0), (64, 1), (64, 2), (64, 3), (64, 4), (64, 5), (64, 6), (64, 7), (64, 8), (64, 9), (64, 10), (64, 11), (64, 12), (64, 13), (64, 14), (64, 15), (64, 16), (64, 17), (64, 18), (64, 19), (64, 20), (64, 21), (64, 22), (64, 23), (64, 24), (64, 25), (64, 26), (64, 27), (64, 28), (64, 29), (64, 30), (64, 31)], [(80, 8), (80, 9), (80, 10), (80, 11), (80, 12), (80, 13), (80, 14), (80, 15), (80, 16), (80, 17), (80, 18), (80, 19), (80, 20), (80, 21), (80, 22), (80, 23), (80, 24), (80, 25), (80, 26), (80, 27), (80, 28), (80, 29), (80, 30), (80, 31), (80, 32), (80, 33), (80, 34), (80, 35), (80, 36), (80, 37), (80, 38), (80, 39), (80, 40), (80, 41), (80, 42), (80, 43), (80, 44), (80, 45), (80, 46), (80, 47)]]
class Obj():
    def __init__(self):
        self.x = 50
        self.y = 50

player = Obj()

print(Movement.createWaypoint(player,walls,(100,50),(5,25)))