'''
exceptions file for any possible exceptions during simulations
'''

class ObjectInsideWall(Exception):
    '''
    if an object (powerup or human) moves or spawns on top of a wall
    '''

class WallOverlapError(Exception):
    '''
    if another wall spawns on top of another wall
    '''

class TraversabilityError(Exception):
    '''
    if the randomly generated wall becomes untraversable (players are not able to move to the other side of the map
    '''