import sys
import os #for debugging
from world import *
from characters import *
import random
import matplotlib.pyplot as plt

rickroll = False

# these variables are able to change without affecting the code, or you can use command line arguments
valueDict = {
    'height' : 50,
    'length' : 100,
    'wallcount' : 5,
    'playernames' : ['Jhon','Nic','Jayden','Josh','Dylan','Christian'],
    'huntchance' : 0.10,
    'sleepchance' : 0.10,
    'headstart' : 10,
    'wolfspawnx' : None,
    'wolfspawny' : None
}
# -----------------[command line arguments]----------------------------------------
args = {}
if len(sys.argv) > 1:
    for args in sys.argv:
        if args == 'main.py':
            pass
        else:
            try:
                key,val = args.split('=')
                valueDict[key] = int(val)
            except TypeError:
                print('Error: invalid integer')

HEIGHT = valueDict['height']
LENGTH = valueDict['length']
WALLCOUNT = valueDict['wallcount']
PLAYERNAMES = valueDict['playernames']
HUNTCHANCE = valueDict['huntchance']
SLEEPCHANCE = valueDict['sleepchance']
HEADSTART = valueDict['headstart']
WOLFSPAWNX = valueDict['wolfspawnx']
WOLFSPAWNY = valueDict['wolfspawny']

#
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
    try:
        plt.scatter(xPlot,yPlot,20,cPlot)
    except UnboundLocalError:
        pass
def plot_hunter(hunter):
    
    plt.scatter(hunter.x,hunter.y,50,"red","s")

def main():
    if rickroll:
        os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    headstartCounter = HEADSTART
    wolfSpawnX = WOLFSPAWNX
    wolfSpawnY = WOLFSPAWNY
    hunt = False
    rawWalls = []
    playerList = []
    wolf = Wolf(WORLDLIMITS,wolfSpawnX,wolfSpawnY)
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
        if hunt is not True:
            plt.title(f"The wolf is sleeping...")

        plot_walls(wallList)
        plot_humans(playerList)
        plot_hunter(wolf)

        if hunt is not True:
            for h in playerList:
                try:
                    h.runSafe()
                except: #catch error if there are no possible moves
                    return
        if headstartCounter == 0:     
            if round(random.random(),2) < HUNTCHANCE: #10% chance
                hunt = True
        
        if hunt:
            plt.title("The hunt begins! The wolf has now awakened!")

            for h in playerList:
                if h.x > GAMEAREA[0]/2:
                    h.runaway()
                else:
                    h.runSafe()
#players must run away first before wolf moves in order for hitreg to work
            if len(playerList) > 0:
                targetObject = wolf.hunt(playerList)


            if (wolf.x,wolf.y) == (targetObject.x,targetObject.y):
                playerList.remove(targetObject)
                targetObject.alive = False

            if round(random.random(),2) < SLEEPCHANCE: #72% chance of going back to sleep
                hunt = False
        #checks if all the players are safe
        safeCount = 0
        for h in playerList:
            if h.safe == True:
                safeCount += 1
                
                if safeCount == len(playerList):
                    print("All players ran away, wolf wins!")
                    return
        # matplotlib code -- do not change --
        plt.xlim(0,LENGTH)
        plt.ylim(0,HEIGHT)
        plt.pause(0.5)
        plt.clf()

        if headstartCounter > 0:
            headstartCounter -= 1
        
if __name__ == "__main__":
    main()