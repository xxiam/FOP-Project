from venv import create
from characters import *
from movement import *
from world import *
import matplotlib.pyplot as plt

worldLimits = (50,50)

wallAmount = 20
objectiveAmount = 5
#refer to dataset.txt for formatting

def plot_walls(wallList):
    print(wallList)
    xlist = []
    ylist = []

    for x,y in wallList:
        xlist.append(x)
        ylist.append(y)

    plt.scatter(xlist,ylist,40,"black","s")

def plot_objective(itemPos):
    xlist = []
    ylist = []

    for x,y in itemPos:
        xlist.append(x)
        ylist.append(y)

    plt.scatter(xlist,ylist,40,"black","s")

def plot_humans(humans):
    xlist = []
    ylist = []
    colours = []
    names = []

    for _ in range(len(humans)):
        xlist.append(humans[_].x)
        ylist.append(humans[_].y)
        colours.append(_)
        names.append(humans[_].name)
        plt.annotate(names[_],(xlist[_],ylist[_]))

    plt.scatter(xlist,ylist,30,colours,'c')
    
        


def main():
    wallDict = {}
    wallList = []
    itemPos = [] 
    humanNames = ['jhon','nic','dylan','jayden','christian']
    humans = []
    for _ in range(wallAmount):
        o,w = World.create_wall(sum(worldLimits)*0.4,worldLimits)
        wallDict[(o,_)] = w

        for v in wallDict.values():
            for xy in v:
                wallList.append(xy)

    
    for _ in range(objectiveAmount):
        itemPos.append(World.create_objective(worldLimits,wallList))

    for _ in range(len(humanNames)):
        humans.append(Human(worldLimits,humanNames[_]))

    while True:
        plot_walls(wallList)
        plot_objective(itemPos)

        for h in range(len(humans)):
            Movement.find(humans[h],itemPos,wallDict,worldLimits)

        plot_humans(humans)
        

#           -- do not change this --
        plt.title(f"{worldLimits[0]} x {worldLimits[1]} map")
        plt.xlim(-1,worldLimits[0])
        plt.ylim(-1,worldLimits[1])
        plt.pause(0.5)
        plt.clf()

if __name__ == "__main__":
    main()