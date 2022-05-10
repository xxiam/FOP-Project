import random

class World():
    
    def create_wall(maxlength,limits):
        '''
        maxlength : usually a certain percentage of the worlds total dot count
        limits : sets the range for the function to randomly create walls
        '''
        orientation = random.randint(0,1)
        start = (random.randint(1,limits[0]),random.randint(1,limits[1]))
        length = random.randint(1,maxlength)

        wallFill = []

        if orientation == 0: #horiozontal wall
            for _ in range(length):
                wallFill.append((start[0] + _, start[1]))
        
        if orientation == 1: #vertical wall
            for _ in range(length):
                wallFill.append((start[0], start[1] + _))

        return orientation,wallFill

    def create_objective(limits,walls):
        
        randomPos = (random.randint(1,limits[0]),random.randint(1,limits[1]))

        if randomPos in walls:
            repeat = True

            while repeat == True:
                randomPos = (random.randint(1,limits[0]),random.randint(1,limits[1]))
                if randomPos not in walls:
                    break
        
        return randomPos
