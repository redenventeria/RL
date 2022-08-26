

from level import Level
from entity import Wall


class Builder:

    def __init__(self, **kwargs):
        pass

    def build(self, **kwargs):
        pass


class BoxBuilder(Builder):

    def __init__(self, *, x: int, y: int, w: int, h: int, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def build(self, level: Level, x_offset=0, y_offset=0):
        for x in range(self.x, self.x + self.w):
            level.add_entity(Wall(x=x, y=self.y))
            level.add_entity(Wall(x=x, y=self.y + self.h))
        for y in range(self.y + 1, self.y + self.y + self.h - 1):
            level.add_entity(Wall(x=self.x, y=y))
            level.add_entity(Wall(x=self.x + self.w, y=y))