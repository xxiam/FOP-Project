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
    'playernames' : ['Jhon','Nic','Jayden','Josh','Dylan','Christian','Kelly'],
    'huntchance' : 0.10,
    'sleepchance' : 0.10,
    'headstart' : 10,
    'wolfspawnx' : None,
    'wolfspawny' : None
}
# -----------------[command line arguments]----------------------------------------
if len(sys.argv) > 1:
    for args in sys.argv:
        if args == 'main.py':
            pass
        else:
            key,val = args.split('=')
            try:
                valueDict[key] = int(val)
            except ValueError:
                try:
                    valueDict[key] = float(val)
                except ValueError:
                    print("Error: invalid format, using default values")
#------------------------------------------------------------------------------------
HEIGHT = valueDict['height']
LENGTH = valueDict['length']
WALLCOUNT = valueDict['wallcount']
PLAYERNAMES = valueDict['playernames']
HUNTCHANCE = valueDict['huntchance']
SLEEPCHANCE = valueDict['sleepchance']
HEADSTART = valueDict['headstart']
WOLFSPAWNX = valueDict['wolfspawnx']
WOLFSPAWNY = valueDict['wolfspawny']

if WOLFSPAWNY is None:
    WOLFSPAWNY = int(HEIGHT/2)
if WOLFSPAWNX is None:
    WOLFSPAWNX = 5
#
GAMEAREA = (LENGTH - 20, HEIGHT)
WALLSPACING = int(GAMEAREA[0]/WALLCOUNT)
WORLDLIMITS = (LENGTH,HEIGHT)
SAFE = (5,HEIGHT/2)

def plot_walls(walls):
    
    xPlot = []
    yPlot = []
    
    for w in walls:
        for x,y in w:
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
    try:
        if rickroll: #this is a joke
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

            plot_walls(wallList)
            plot_humans(playerList)
            plot_hunter(wolf)

            if hunt is not True:
                plt.title(f"The wolf is sleeping...")

                for h in playerList:
                    try:
                        h.runSafe()
                    except PlayerSafeZone as e:
                        print(e)
                        return

            if headstartCounter == 0:     
                if round(random.random(),2) < HUNTCHANCE: #10% chance
                    hunt = True
            
            if hunt:
                if round(random.random(),2) < SLEEPCHANCE: 
                    hunt = False

                plt.title("The hunt begins! The wolf has now awakened!")

                for h in playerList:
                    if h.x > GAMEAREA[0]/2:
                        h.runaway()
                    else:
                        h.waypointList = Movement.createWaypoint(h,wallList,WORLDLIMITS,SAFE)
                        h.runSafe()

                #players must run away first before wolf moves in order for hitreg to work
                if len(playerList) > 0:
                    targetObject = wolf.hunt(playerList)


                if (wolf.x,wolf.y) == (targetObject.x,targetObject.y):
                    try:
                        playerList.remove(targetObject)
                        targetObject.alive = False
                    except ValueError:
                        print("All players are dead, Wolf wins!")
                        return

            #checks if all the players are safe
            runawayCount = 0
            for h in playerList:
                if h.ranAway == True:
                    runawayCount += 1
                    
                    if runawayCount == len(playerList):
                        print("All players ran away, wolf wins!")
                        return
                        
            # matplotlib code -- do not change --
            plt.xlim(0,LENGTH)
            plt.ylim(0,HEIGHT)
            plt.pause(0.5)
            plt.clf()

            if headstartCounter > 0:
                headstartCounter -= 1

    except KeyboardInterrupt:
        print("Quitting simulation via KeyboardInterrupt")
        return

if __name__ == "__main__":
    main()