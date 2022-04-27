'''
worldbuilding.py - world building for humans and ghosts
'''
import random

class World(): #finished
    
    def create_wall(num,max,limit):
        '''
        randomly creates <num> walls of <random length> units length at a random place
        max - maximum length of wall
        limit - world borders
        '''
        wall = {}

        for w in range(num):
            length = random.randint(1,max)
            orientation = random.randint(0,1) #0 = horizontal, 1 = vertical

            wallStart = (random.randint(1,limit[0]),random.randint(1,limit[1]))
            if orientation == 0: #horizontal wall
                wallEnd = (wallStart[0] + length, wallStart[1])
            if orientation == 1:
                wallEnd = (wallStart[0], wallStart[1] + length)
            
            wall[(orientation,w)] = [(wallStart),(wallEnd)]
        
        for k,v in wall.items():
            startX = v[0][0]
            startY = v[0][1]
            endX = v[1][0]
            endY = v[1][1]

            if startX == endX:
                for i in range(endY - startY + 1):
                    wall[k].append((startX, startY + i))
            elif startY == startY:
                for i in range(endX - startX + 1):
                    wall[k].append((startX + i, startY))

        return wall
            
    def create_knives(num,limit,walls):
        '''
        randomly creates <num> amount of knives
        limits - avoids placing a knife outside the world borders
        walls - avoids the chance of placing a knife on a wall
        '''
        knife_loc = []

        for k in range(num):
            xy = (random.randint(1,limit[1]),random.randint(1,limit[0]))

            if xy in walls:
                xy = (random.randint(1,limit[1]),random.randint(1,limit[0]))

            knife_loc.append(xy)
            #creates a tuble of (x,y) location

        return knife_loc