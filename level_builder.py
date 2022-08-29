
import random
from typing import TYPE_CHECKING, List, Set, Tuple
from ai import randomAI
from entity import AIEntity, Wall
from level import Level
from prefab_builder import RoomBuilder, Filler
from util import Tile, Vector2D, Rectangle

if TYPE_CHECKING:
    from engine import Engine

class LevelBuilder:

    def __init__(self, dimensions: Vector2D, **kwargs):
        self.dimensions = dimensions

    def build(self, **kwargs):
        raise NotImplementedError()



"""class TestingBox(LevelBuilder):
    def __init__(self, width: int, height: int, **kwargs):
        self.builder = RoomBuilder(x=10, y=10, w=5, h=5)
    
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

        return level"""

class BSPLevelBuilder(LevelBuilder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def build(self, **kwargs):

        filler = Filler(Rectangle(Vector2D(0, 0), self.dimensions))
        level = Level(self.dimensions)
        filler.build(level, 
            lambda position: 
                Wall(position, Tile(" ", (30, 30, 30), (30, 30, 30)))
        )

        self.rectangles: List[Rectangle] = list()
        #self.rectangles.append(Rectangle(1, 1, self.width - 2, self.height - 2))
        self.rectangles.append(Rectangle(Vector2D(1, 1), self.dimensions - Vector2D(2, 2)))

        for i in range(4):
            rect: Rectangle = random.choice(self.rectangles)
            if (rect.dimensions.x - 4)*(rect.dimensions.y - 4) // 4 > 16:
                subRectangles = self.getSubRectangles(rect)
                self.rectangles.remove(rect)
                for rect in subRectangles:
                    self.rectangles.append(rect)
            
        for rect in self.rectangles:

            if random.uniform(0, 1) > 0:
                """randx = random.randint(rect.x, rect.x+rect.width - 5)
                randy = random.randint(rect.y, rect.y+rect.height - 5)
                randwidth = random.randint(4, rect.x + rect.width - randx)
                randheight = random.randint(4, rect.y + rect.height - randy)"""
                x1, y1 = rect.position
                x2, y2 = rect.getOtherPoint()
                position = Vector2D.getRandom(x1, x2 - 5, y1, y2 - 5)
                dimensions = Vector2D.getRandom(4, x2 - position.x, 4, y2 -position.y)
                randomRectangle = Rectangle(position, dimensions)
                builder = RoomBuilder(randomRectangle)
                builder.build(level)
        
        return level
    
    def getSubRectangles(self, rect: Rectangle) -> List[Rectangle]:
        position = rect.position + Vector2D(1, 1)
        dimensions = rect.dimensions - Vector2D(2, 2)
        halfDimensions = dimensions // 2

        positionLeftUp = position + Vector2D(0, 0)
        positionRightUp = position + Vector2D(halfDimensions.x + 1, 0)
        positionLeftDown = position + Vector2D(0, halfDimensions.y + 1)
        positionRightDown = position + Vector2D(halfDimensions.x + 1, halfDimensions.y + 1)

        subRectangles: List[Rectangle] = []
        subRectangles.append(Rectangle(positionLeftUp, halfDimensions))
        subRectangles.append(Rectangle(positionLeftDown, halfDimensions))
        subRectangles.append(Rectangle(positionRightUp, halfDimensions))
        subRectangles.append(Rectangle(positionRightDown, halfDimensions))

        return subRectangles

        