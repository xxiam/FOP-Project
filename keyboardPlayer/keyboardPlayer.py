import keyboard
import matplotlib.pyplot as plt

limits = (100,50)

class KeyboardPlayer():
    def __init__(self,name):
        self.name = name
        self.x = limits[0]/2
        self.y = limits[1]/2

    def moveup(self):
        self.y += 1
        return
    
    def movedown(self):
        self.y -= 1
        return

    def moveleft(self):
        self.x -= 1
        return

    def moveright(self):
        self.x += 1
        return
        
def plotCharacter(character):
    plt.scatter(character.x,character.y,20,'black')

def main():
    
    c = KeyboardPlayer('jhon')
    while True:
        keyboard.on_press_key('w', lambda _:c.moveup())
        keyboard.on_press_key('a', lambda _:c.moveleft())
        keyboard.on_press_key('s', lambda _:c.movedown())
        keyboard.on_press_key('d', lambda _:c.moveright())
        plotCharacter(c)
        plt.xlim(0,limits[0])
        plt.ylim(0,limits[1])
        plt.pause(0.5)
        plt.clf() 

if __name__ == '__main__':
    main()