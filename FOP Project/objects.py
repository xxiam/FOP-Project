'''
objects.py - hunters and hunted classes

ghost class:
at the start of the simulation, the ghosts are hunting the humans,
once the humans find the holy knife, humans can now hunt ghosts,
ghosts can travel through walls and move faster than humans

humans class:
ghost prey, hunted by ghosts until they find the holy knife,
cannot travel through walls and move slower than ghosts,

'''
import random

worldLimits = (100,1000)

class Human():

    def __init__(self, name):
        self.name = name
        self.y = random.randint(0, worldLimits[1] - 1)
        self.x = random.randint(0, worldLimits[0] - 1)
        self.dead = False
        self.felloff = False
        self.speed = 1

    def find(self, item, walls):
        '''
        finds the knife
        item - the location of the knives
        walls - humans cannot walk through walls like ghosts, so they have to walk around it 
        '''

        if self.felloff == True or self.dead == True:
            self.x = -10
            self.y = -10

        else:
            #how to do object avoidance (use same as practest 3 code)
            #if human is within 1 units near a wall
            
            loc_diff = []
            #find the closest knife to the human
            for x,y in item:
                diff_x = self.x - x
                diff_y = self.y - y
                if diff_y < 0:
                    diff_y * -1
                elif diff_x < 0:
                    diff_y * -1
                loc_diff.append((diff_x,diff_y))

            closest_knife = min(loc_diff)

            #move to the closest knfe
            if self.x < closest_knife[0]: #if human is to the left of closest knife
                self.x += self.speed
            if self.y < closest_knife[1]: #if human is under the closest knife
                self.y += self.speed
            if self.x > closest_knife[0]:
                self.x -= self.speed
            if self.y > closest_knife[1]:
                self.y -= self.speed

            #this code allows movement but moves through walls   


    def hunt(self, ghosts, walls):
        '''
        once the knife has been found, the humans can now hunt the ghosts, 
        ghosts will now be slower than humans but can still traverse walls

        ghosts - coordinates of ghosts as they move

        walls - humans still have to avoid walls
        '''