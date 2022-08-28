from level import Level
from entity import Wall



class PrefabBuilder:

    def __init__(self, **kwargs):
        pass

    def build(self, **kwargs):
        pass

class BoxBuilder(PrefabBuilder):

    def __init__(self, *, x: int, y: int, w: int, h: int, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def build(self, level: Level, x_offset=0, y_offset=0):
        i: int = 0
        for x in range(self.x, self.x + self.w):
            level.addEntity(Wall(x=x, y=self.y, fg=(100, 150, 20)))
            level.addEntity(Wall(x=x, y=self.y + self.h - 1, fg=(100, 150, 20)))
        for y in range(self.y + 1, self.y + self.h - 1):
            level.addEntity(Wall(x=self.x, y=y))
            level.addEntity(Wall(x=self.x + self.w - 1, y=y))
        print(i)
    