'''
worldbuilding.py - world building for humans and ghosts
'''
import random

class World(): #finished
    
    def create_obstacles(num,limit):
        '''
        num - how many obstacles will be on the map, random placement
        limit - creates a border to stop random generation of obstacles outside of world limits
        '''
        obstacleLoc = []

        for o in range(num):
            xy = (random.randint(1,limit[1]),random.randint(1,limit[0]))
            obstacleLoc.append(xy)
        
        return obstacleLoc

    def create_wall(num,max,limit):
        '''
        randomly creates <num> walls of <random length> units length at a random place
        max - maximum length of wall
        limit - world borders
        '''
        wall_loc = []
        wall_fill = []

        for w in range(num):
            length = random.randint(1,max) #creates random length
            
            #random placement of x, y direction
            xy = random.randint(0,1)
            if xy == 0: #wall of x direction
                wall_start = (random.randint(1,limit[1]),random.randint(1,limit[0])) #x,y pos
                wall_end = (wall_start[0] + length, wall_start[1]) #x,y pos
            if xy == 1: #wall of y direction
                wall_start = (random.randint(1,limit[1]),random.randint(1,limit[0])) #xy pos
                wall_end = (wall_start[0], wall_start[1] + length)
            
            wall_loc.append((wall_start,wall_end)) #appends locations of wall as a tuple
            #should look something like [((start x, start y),(end x, end y))]

        #wall_fill, rest of the coordinates that will be considered as a wall
        for _ in wall_loc: #should look something like ((start x, start y),(end x, end y))
            start_x = _[0][0] 
            start_y = _[0][1]

            end_x = _[1][0]
            end_y = _[1][1]

            if start_x == end_x: #if the wall is vertical
                wall_fill.append((start_x,start_y))
                for i in range(end_y - start_y + 1):
                    wall_fill.append((start_x,start_y + i))

            elif start_y == end_y: #if the wall is horizontal
                wall_fill.append((start_x,start_y))
                for i in range(end_x - start_x + 1):
                    wall_fill.append((start_x + i, start_y))
        
        return wall_fill
        
    def create_knives(num,limit,obstacles,walls):
        '''
        randomly creates <num> amount of knives
        limits - avoids placing a knife outside the world borders
        obstacles - avoids the chance of placing a knife on an obstacle
        walls - avoids the chance of placing a knife on a wall
        '''
        knife_loc = []

        for k in range(num):
            xy = (random.randint(1,limit[1]),random.randint(1,limit[0]))

            if xy in obstacles or xy in walls:
                xy = (random.randint(1,limit[1]),random.randint(1,limit[0]))

            knife_loc.append(xy)
            #creates a tuble of (x,y) location

        
        return knife_loc