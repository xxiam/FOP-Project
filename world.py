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
        

    def create_objective(num,limits, walls):
        '''
        limits: confines objective inside simulation limits
        walls: avoids spawning inside walls (should be passed in as a single list with tuples of wall locations)
        '''
        objectivePos = []

        for _ in range(num):
            randomPos = (random.randint(1,limits[0]),random.randint(1,limits[1]))
            if randomPos in walls:
                objective = (randomPos[0] + 1, randomPos[1] + 1) # move diagonally
            else:
                objective = randomPos
            objectivePos.append(objective)

        return objectivePos
        
        
class Counter(): #this will count how many times a function has been called
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self,*args,**kwargs):
        self.counter += 1
        return self.func(*args,**kwargs)