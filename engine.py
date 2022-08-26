import random
from tcod.console import Console
from event_handler import EventHandler
from action_handler import ActionHandler
from entity import Empty
from entity import Entity
from entity import Wall
from level import Level
from level_bulder import BoxBuilder

class Engine():
    def __init__(self, console: Console) -> None:
        self.width = console.width
        self.height = console.height
        self.console = console

        self.player = Entity(is_solid=True, char="@", x=44, y=30)

        self.eventHandler = EventHandler()
        self.actionHandler = ActionHandler(self)

        self.console.clear()

        self.current_level = Level(width=self.width, height=self.height)
        
        self.build_level()
    
    def build_level(self):
        box = BoxBuilder(x=3, y=3, w=10, h=10)
        box.build(self.current_level)
        
        

    def draw(self) -> None:
        for i in range(self.width):
            for j in range(self.height):
                cell = self.curlevel[i][j]
                self.console.print(i, j, cell.tile, fg=cell.fg, bg=cell.bg)
        self.console.print(self.player.x, self.player.y, "@")
