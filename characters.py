'''
    character classes for humans and wolves,
    wolves have a significantly higher movement speed than humans, they can also jump over walls
'''
import random
import math
from movement import *
import os

class Human():
    def __init__(self,limits,name):
        self.name = name
        self.x = limits[0] - 5
        self.y = random.randint(1,limits[1])
        self.speed = 1
        self.waypointList = None
        self.waypoint = (None,None)
        self.alive = True
        self.safe = False
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
            pass 
    
        ### movement code ### do not douch ###
        if self.x > waypoint[0]:
            self.x -= self.speed
        if self.x < waypoint[0]:
            self.x += self.speed
        if self.y > waypoint[1]:
            self.y -= self.speed
        if self.y < waypoint[1]:
            self.y += self.speed

        self.prevMoves.append((self.x,self.y))

    def runaway(self):
        try:
            waypoint = self.prevMoves[-1]
        except IndexError:
            pass
        if self.safe is False:
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
                self.safe = True #there is nowhere for the player to move therefore raising the error

        if (self.x,self.y) == waypoint:
            self.prevMoves.remove(self.waypointList[-1])

class Wolf():

    def __init__(self,limits):
        self.x = 5
        self.y = int(limits[1])/2
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

        closestPlayer = humans[hypdiff.index(min(hypdiff))]

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