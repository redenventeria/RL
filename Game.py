import random
from tcod.console import Console
import numpy
from EventHandler.EventHandler import EventHandler
from ActionHandler.ActionHandler import ActionHandler
from GameObjects.Empty import Empty
from GameObjects.GameObject import GameObject
from GameObjects.Wall import Wall

class Game():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.console = Console(width, height)

        self.player_x = 30
        self.player_y = 30

        self.eventHandler = EventHandler()
        self.actionHandler = ActionHandler(self)

        self.console.clear()

        self.level: list[list[GameObject]] = [
            [Empty() for j in range(self.width)] 
            for i in range(self.height)
        ]
        self.build_level()
    
    def build_level(self):
        for i in range(self.height):
            for j in range(self.width):
                self.level[i][j] = random.choice([Empty(), Empty(), Empty(), Wall()])
        

    def draw(self) -> None:
        for i in range(self.width):
            for j in range(self.height):
                cell = self.level[i][j]
                self.console.print(i, j, cell.tile, fg=cell.fg, bg=cell.bg)
        self.console.print(self.player_x, self.player_y, "@")


g = Game(30, 30)
g.draw()