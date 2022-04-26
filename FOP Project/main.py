from objects import *
from worldbuilding import *
import random
import matplotlib.pyplot as plt
import numpy as np

limits = (1000,1000) #height, length of map (y,x)

def plot_walls(walls):
    xlist = []
    ylist = []

    for x,y in walls:
        xlist.append(x)
        ylist.append(limits[0] - y - 1)
    plt.scatter(xlist,ylist,c="black",marker="s",s=10)

def plot_obstacles(obstacles):
    X = []
    Y = []

    for x,y in obstacles:
        X.append(x)
        Y.append(limits[0] - y - 1)
    plt.scatter(X,Y,c="black",s=10)

def plot_knives(knives):
    X = []
    Y = []

    for x,y in knives:
        X.append(x)
        Y.append(limits[0] - y - 1)
    plt.scatter(X,Y,c="green",s=40)

def plot_humans(humans,limit,walls,obstacles):
    xlist = []
    ylist = []
    slist = [40]
    clist = []
    blocks = []

    for w in walls:
        blocks.append(w)
    for o in obstacles:
        blocks.append(o)

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
    obstacles = World.create_obstacles(num=100,limit=limits)
    walls = World.create_wall(num=200,max=50,limit=limits)
    knives = World.create_knives(num=5,limit=limits,obstacles=obstacles,walls=walls)
    humans = []

    for n in range(len(names)):
        humans.append(Human(names[n]))

    while True:
        
        plot_walls(walls)
        plot_obstacles(obstacles)
        plot_knives(knives)

        for h in range(len(humans)):
            humans[h].find(knives,walls,obstacles)

        plot_humans(humans,limits,walls,obstacles)

        plt.title("1000,1000 map")
        plt.ylabel("y")
        plt.xlabel("x")
        plt.xlim(-1,limits[1])
        plt.ylim(-1,limits[0])
        plt.pause(0.05)
        plt.clf()

if __name__ == "__main__":
    main()