'''
worldbuilding.py - world building for humans and ghosts
'''
import random

class World(): 

    def create_wall(num,max,limit):
        '''
        randomly creates <num> walls of <random length> units length at a random place
        max - maximum length of wall
        limit - world borders
        when rewriting, make sure to format it in {(orientation,number) : [(walstart),...(wallend)]}
        '''
        walls = {}
        for n in range(num):
            start = (random.randint(1,limit[0]),random.randint(1,limit[1]))
            orientation = random.randint(0,1)
            length = random.randint(1,max)
            
            walls[(orientation,n)] = [start]

            if orientation == 0: #horizontal
                end = (start[0] + length, start[1])
                for _ in range(end[0] - start[0] + 1):
                    walls[(orientation,n)].append((start[0] + _,start[1]))

            if orientation == 1: #vertial
                end = (start[0], start[1] + length)
                for _ in range(end[1] - start[1] + 1):
                    walls[(orientation,n)].append((start[0], start[1] + _))

        return walls
            
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
# %%
