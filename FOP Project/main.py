from objects import *
from worldbuilding import *
import random
import matplotlib.pyplot as plt
import numpy as np

limits = (50,50) #height, length of map (x,y)

def plot_walls(walls):
    xlist = []
    ylist = []
    wallDetails = []
    for k,v in walls.items():
        for x,y in v:
            xlist.append(x)
            ylist.append(y)
        wallDetails.append(k)

    plt.scatter(xlist,ylist,c="black",marker="s",s=10)

def plot_knives(knives):
    X = []
    Y = []

    for x,y in knives:
        X.append(x)
        Y.append(limits[0] - y - 1)
    plt.scatter(X,Y,c="green",s=40)

def plot_humans(humans,limit,walls):
    xlist = []
    ylist = []
    slist = [40]
    clist = []
    blocks = []

    for w in walls:
        blocks.append(w)

    for h in range(len(humans)):
        ylist.append(limit[0] - humans[h].y - 1)
        xlist.append(humans[h].x)
        clist.append(h) 
        plt.annotate(humans[h].name, (xlist[h] + 1, ylist[h] + 1))

        while (xlist[h],ylist[h]) in blocks: #if human randomly spawns inside a wall or obstacle
            xlist[h] += 1
            ylist[h] += 1
            
    plt.scatter(xlist,ylist,s=slist,c=clist)

def main():
    names = ["jhon","nic","dylan","jayden","christian"]
    walls = World.create_wall(num=int(limits[0]*0.5),max=int(limits[0]*0.5),limit=limits)
    knives = World.create_knives(num=5,limit=limits,walls=walls)
    humans = []

    for n in range(len(names)):
        humans.append(Human(names[n], limits))

    while True:
        
        plot_walls(walls)
        plot_knives(knives)

        for h in range(len(humans)):
            Movement.find(humans[h],knives,walls)

        plot_humans(humans,limits,walls)

        plt.title(f"{limits[0]} , {limits[1]} map")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.xlim(-1,limits[1])
        plt.ylim(-1,limits[0])
        plt.pause(0.5)
        plt.clf()

if __name__ == "__main__":
    main()