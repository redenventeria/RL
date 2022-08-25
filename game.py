import random
from tcod.console import Console
from event_handler import EventHandler
from action_handler import ActionHandler
from game_object import Empty
from game_object import GameObject
from game_object import Wall

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