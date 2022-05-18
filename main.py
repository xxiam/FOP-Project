
from world import *
from characters import *
import random
import matplotlib.pyplot as plt

# these variables are able to change without affecting the code
HEIGHT = 50
LENGTH = 100
WALLCOUNT = 5
NUMOBJ = 5
PLAYERNAMES = ["Jhon","Nic","Jayden","Josh","Dylan","Christian"] 
# -------------------------------------------------------------

GAMEAREA = (LENGTH - 20, HEIGHT)
WALLSPACING = int(GAMEAREA[0]/WALLCOUNT)
WORLDLIMITS = (LENGTH,HEIGHT)
SAFE = (10,HEIGHT/2)

def plot_walls(walls):
    
    xPlot = []
    yPlot = []
    
    rawWalls = []

    for w in walls:
        for i in w:
            rawWalls.append(i)

    for x,y in rawWalls:
        xPlot.append(x)
        yPlot.append(y)
    
    plt.scatter(xPlot,yPlot,20,"black","s")

def plot_humans(humans):

    xPlot = []
    yPlot = []
    
    for h in humans:
        xPlot.append(h.x)
        yPlot.append(h.y)
        cPlot = list(range(len(humans)))
        plt.annotate(h.name,(h.x,h.y))
    plt.scatter(xPlot,yPlot,20,cPlot)
    
def plot_hunter(hunter):
    
    plt.scatter(hunter.x,hunter.y,50,"red","s")

def main():
    hunt = []
    rawWalls = []
    playerList = []
    wolf = Wolf(WORLDLIMITS)
    wallList = Worldbuilding.create_wall(WALLCOUNT,int(0.8*GAMEAREA[1]),GAMEAREA,WALLSPACING)

    for n in PLAYERNAMES:
        playerList.append(Human((LENGTH,HEIGHT),n))

    for x in wallList:
        for i in x:
            rawWalls.append(i)

    for player in playerList:
        waypointList = Movement.createWaypoint(player,wallList,WORLDLIMITS,SAFE)
        player.waypointList = waypointList

        if len(playerList) == 0:
            print("All players have now been killed by the wolf!")
            return

    while True:

        os.system('cls')
        
        if hunt is not True:
            plt.title(f"The wolf is sleeping...")

        plot_walls(wallList)
        plot_humans(playerList)
        plot_hunter(wolf)

        if hunt is not True:
            for h in playerList:
                h.runSafe()

        if round(random.random(),2) < 0.10: #10% chance
            hunt = True
            
        if hunt:
            targetObject = wolf.hunt(playerList)
            plt.title("The hunt begins! The wolf has now awakened!")

            for h in playerList:
                h.runaway()

            if (wolf.x,wolf.y) == (targetObject.x,targetObject.y):
                playerList.remove(targetObject)
                targetObject.alive = False

        # matplotlib code -- do not change --
        plt.xlim(0,LENGTH)
        plt.ylim(0,HEIGHT)
        plt.pause(0.5)
        plt.clf()


    

if __name__ == "__main__":
    main()