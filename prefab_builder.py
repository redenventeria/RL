from curses.textpad import rectangle
from typing import Callable
from level import Level
from entity import Empty, Entity, Wall
from util import Vector2D, Rectangle



class PrefabBuilder:

    def __init__(self, **kwargs):
        pass

    def build(self, **kwargs):
        pass

class RoomBuilder(PrefabBuilder):

    def __init__(self, rectangle: Rectangle, **kwargs):
        super().__init__(**kwargs)
        self.rectangle = rectangle

    def build(self, level: Level, x_offset=0, y_offset=0):
        i: int = 0
        x1, y1 = self.rectangle.position
        x2, y2 = self.rectangle.getOtherPoint()
        for x in range(x1, x2):
            level.addEntity(Empty(Vector2D(x, y1)))
            level.addEntity(Wall(Vector2D(x, y1)))
            level.addEntity(Empty(Vector2D(x, y2 - 1)))
            level.addEntity(Wall(Vector2D(x, y2 - 1)))
        for y in range(y1 + 1, y2 - 1):
            level.addEntity(Empty(Vector2D(x1, y)))
            level.addEntity(Wall(Vector2D(x1, y)))
            level.addEntity(Empty(Vector2D(x2 - 1, y)))
            level.addEntity(Wall(Vector2D(x2 - 1, y)))
        
        #filler = Filler(x=self.x+1, y=self.y+1, w=self.w - 2, h=self.h - 2)
        filler = Filler(
            Rectangle(
                self.rectangle.position + Vector2D(1, 1),
                self.rectangle.dimensions - Vector2D(2, 2)
            )
        )
        filler.build(level, Empty)
    
class Filler(PrefabBuilder):
    def __init__(self, rectangle: Rectangle, **kwargs):
        super().__init__(**kwargs)
        self.rectangle = rectangle
    
    def build(self, level: Level, fill_function: Callable, x_offset=0, y_offset=0, **kwargs):
        x1, y1 = self.rectangle.position
        x2, y2 = self.rectangle.getOtherPoint()
        for x in range(x1, x2):
            for y in range(y1, y2):
                level.addEntity(fill_function(Vector2D(x, y)))
        
        return level