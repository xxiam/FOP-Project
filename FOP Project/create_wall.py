import random

def create_wall(num,max,limit):
    wall = {} #{(wallOrientation, wallNumber) : [(x,y),(x,y)]}

    for w in range(num):
        length = random.randint(1,max)
        xy = random.randint(0,1) #0 = x, 1 = y

        wallStart = (random.randint(1,limit[0]),random.randint(1,limit[1]))
        if xy==0:
            wallEnd = (wallStart[0] + length, wallStart[1])
        if xy==1:
            wallEnd = (wallStart[0], wallStart[1] + length)
        
        wall[(xy,w)] = [(wallStart),(wallEnd)]
        #wall should look something like {(0,1):[(x,y),(x,y)]}

    for k,v in wall.items():
        startX = v[0][0]
        startY = v[0][1]

        endX = v[1][0]
        endY = v[1][1]

        if startX == endX: #if the wall is vertical
            for i in range(endY - startY+1):
                wall[k].append((startX,startY+i))

        elif startY == endY: #if the wall is horizontal
            for i in range(endX - startX+1):
                wall[k].append((startX+i,startY))

    return wall

w = create_wall(10,5,(100,100))

for k,v in w.items():
    print(k)
    print(v)
    print('\n')

        
        