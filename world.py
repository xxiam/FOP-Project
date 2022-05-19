import random

class Worldbuilding():

    def create_wall(numWalls,length,gameArea,spacing):
        '''
        numWalls : how many walls are going to be created
        length : how long the walls are going to be made
        limits: stops walls from being created outside the simulation borders
        '''
        #length will be passed in as as an integer
        #limits will be passed in as a tuple
        wallList = []
        x = spacing
        maxHeight = gameArea[1]

        for _ in range(numWalls):
            temp = []
            wallStart = (x,random.randint(0,gameArea[1]))
            y = wallStart[1]
            x += spacing
            for _ in range(length):
                wallFill = (wallStart[0],y)     
                y += 1
                temp.append(wallFill)
                if y > maxHeight:
                    y = 0
            wallList.append(temp)
            
        return wallList