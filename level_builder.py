
import random
from re import X
from secrets import choice
from typing import TYPE_CHECKING, List, Set, Tuple
from ai import randomAI
from entity import AIEntity
from level import Level
from prefab_builder import BoxBuilder

if TYPE_CHECKING:
    from engine import Engine

class LevelBuilder:

    def __init__(self, width: int, height: int, **kwargs):
        self.width = width
        self.height = height

    def build(self, **kwargs):
        raise NotImplementedError()



class TestingBox(LevelBuilder):
    def __init__(self, width: int, height: int, **kwargs):
        self.builder = BoxBuilder(x=10, y=10, w=5, h=5)
    
    def build(self, *, engine: "Engine", **kwargs) -> Level:
        level = Level(width=self.width, height=self.height)
        # self.builder.build(level)
        for i in range(20):
            x=random.randint(0, engine.width - 1)
            y=random.randint(0, engine.height - 1)
            bg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            fg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            test_monster = AIEntity(
                is_solid=True,
                is_blocking_fov=False,
                char=random.choice("qwertyuiopasdfghjklzxcvbnm"),
                fg=fg,
                bg=bg,
                x=x,
                y=y,
                priority=10,
                ai=randomAI(),
                engine=engine,
                actionPoints=100,
                hp=15,
                attack=3
            )
            level.addEntity(test_monster)

        return level

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
class BSPLevelBuilder(LevelBuilder):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def build(self, **kwargs):

        self.rectangles: List[Rectangle] = list()
        self.rectangles.append(Rectangle(1, 1, self.width - 2, self.height - 2))

        for i in range(8):
            rect: Rectangle = random.choice(self.rectangles)
            if (rect.width - 4)*(rect.height - 4) // 4 > 16:
                subRectangles = self.getSubRectangles(rect)
                self.rectangles.remove(rect)
                for rect in subRectangles:
                    self.rectangles.append(rect)
            

        level = Level(width=self.width, height=self.height)
        for rect in self.rectangles:

            """builder_debug = BoxBuilder(x=rect.x, y=rect.y, w=rect.width, h=rect.height)
            builder_debug.build(level)"""

            if random.uniform(0, 1) > 0.1:
                randx = random.randint(rect.x, rect.x+rect.width - 5)
                randy = random.randint(rect.y, rect.y+rect.height - 5)
                randwidth = random.randint(4, rect.x + rect.width - randx)
                randheight = random.randint(4, rect.y + rect.height - randy)
                builder = BoxBuilder(x=randx, y=randy, w=randwidth, h=randheight)
                builder.build(level)
        
        return level
    
    def getSubRectangles(self, rect: Rectangle) -> List[Rectangle]:
        x = rect.x + 1
        y = rect.y + 1
        width = rect.width - 2
        height = rect.height - 2
        hwidth = width // 2
        hheight = height // 2

        subRectangles: List[Rectangle] = []
        subRectangles.append(Rectangle(x, y, hwidth, hheight))
        subRectangles.append(Rectangle(x + hwidth + 1, y, hwidth, hheight))
        subRectangles.append(Rectangle(x, y + hheight + 1, hwidth, hheight))
        subRectangles.append(Rectangle(x + hwidth + 1, y + hheight + 1, hwidth, hheight))

        return subRectangles

        