# FOP-Project
A variant of "Whats the time, Mr. Wolf", a simulation of humans (players) and a wolf object running away or running past the wolf in order to win.

Inside the folder:

    Files:
        - main.py : main file handling most variables and plotting in pyplot
        - characters.py : class files for both players and wolf objects and respective movement methods
        - movement.py : class file for players using a waypoint system in order to traverse through the simulation
        - world.py : class file for worldbuilding, randomly generated walls at specified intervals

Modules used:

    Dependancies:
        - os : used for debugging, usually used for os.system("sleep") methods in order to access variables during the running of simulations
        - random : used for randomly generating walls
        - sys : used for command line arguments to change any values in the simulation
        - math : mainly using math.hypot() to calculate the shortest path for players to follow

Information to run the program:
    
    The code allows the manipulation of certain variables such as:
        - height of simulation map
        - length of simulation map
        - amount of walls to be made
        - player names and player count (however, this needs to be directly changed in main.py, line 15)
            the amount of players will be determined by how many names are in the list
        - % chance of the wolf huting players
        - % chance of the wolf falling back asleep
        - the amount of time players have a headstart before the % chance the wolf wakes up
        - the location of the wolf spawning
    
    All of these can be changed (apart from player count/names) using command line arguments

    Example: /the order of command line argumes do not need to be in order/
    
        - python3 main.py
        - python3 main.py length=100 height=500 headstart=50
