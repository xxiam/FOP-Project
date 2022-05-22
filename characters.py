'''
    character classes for humans and wolves,
    wolves have a significantly higher movement speed than humans, they can also jump over walls
'''
import random
import math
from movement import *

class Human():
    def __init__(self,limits,name):
        self.name = name
        self.x = limits[0]
        self.y = random.randint(1,limits[1])
        self.speed = 1
        self.waypointList = None
        self.waypoint = (None,None)
        self.alive = True
        self.ranAway = False
        self.prevMoves = []

    def runSafe(self):
        
        '''
        safe : other side of the map
        walls : walls to avoid
        limits : humans can fall off the map
        '''
        try:
            waypoint = self.waypointList[-1]
            if (self.x,self.y) == waypoint:
                self.waypointList.remove(self.waypointList[-1])
        except IndexError: 
            pass #allows the player to reach the safe zone without causing an error
    
        ### movement code ### do not douch ###
        try:
            if self.x > waypoint[0]:
                self.x -= self.speed
            if self.x < waypoint[0]:
                self.x += self.speed
            if self.y > waypoint[1]:
                self.y -= self.speed
            if self.y < waypoint[1]:
                self.y += self.speed
        except UnboundLocalError:
            raise PlayerSafeZone(f"{self.name} has won the game for all players! players win!")

        self.prevMoves.append((self.x,self.y))

    def runaway(self):
        try:
            waypoint = self.prevMoves.pop()
        except IndexError:
            pass
        if self.ranAway is False:
            try:
                if self.x > waypoint[0]:
                    self.x -= self.speed
                if self.x < waypoint[0]:
                    self.x += self.speed
                if self.y > waypoint[1]:
                    self.y -= self.speed
                if self.y < waypoint[1]:
                    self.y += self.speed
            except UnboundLocalError:
                self.ranAway = True #there is nowhere for the player to move therefore raising the error

class Wolf():

    def __init__(self,limits,xSpawn,ySpawn):
        
        self.x = xSpawn
        self.y = ySpawn
        
        self.speed = 5

    def hunt(self,humans):
        '''
        humans : positions of humans
        '''
        
        humanPos = []

        for players in humans:
            humanPos.append((players.x,players.y))

        hypdiff = []
        for x,y in humanPos:
            xdiff = self.x - x
            ydiff = self.y - y

            if xdiff < 0:
                xdiff *= -1
            if ydiff < 0:
                ydiff *= -1

            hypdiff.append(math.hypot(xdiff,ydiff))
        try:
            closestPlayer = humans[hypdiff.index(min(hypdiff))]
        except ValueError:
            raise NoActivePlayers("All players have been killed by the wolf! Wolf wins!")

        ##movement code
        distance = closestPlayer.x - self.x
        if distance < 0:
            distance *= -1

        if distance > 5: 
            if self.x > closestPlayer.x:
                self.x -= self.speed
            if self.x < closestPlayer.x:
                self.x += self.speed
            if self.y > closestPlayer.y:
                self.y -= self.speed
            if self.y < closestPlayer.y:
                self.y += self.speed

        if distance < 5:
            if self.x > closestPlayer.x:
                self.x -= distance
            if self.x < closestPlayer.x:
                self.x += distance
            if self.y > closestPlayer.y:
                self.y -= distance
            if self.y < closestPlayer.y:
                self.y += distance
        
        return closestPlayer

class PlayerSafeZone(Exception):
    pass
'''
if a player reaches the safe zone, all players win
'''

class NoActivePlayers(Exception):
    pass
'''
raises error if there are no more players
'''