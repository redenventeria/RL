
import random
from typing import TYPE_CHECKING
from ai import randomAI
from entity import AIEntity, Entity
from level import Level
from prefab_builder import BoxBuilder

if TYPE_CHECKING:
    from engine import Engine

class LevelBuilder:

    def __init__(self, width: int, height: int, **kwargs):
        raise NotImplementedError()

    def build(self, **kwargs):
        raise NotImplementedError()



class TestingBox(LevelBuilder):
    def __init__(self, width: int, height: int, **kwargs):
        self.builder = BoxBuilder(x=10, y=10, w=5, h=5)
        self.width = width
        self.height = height
    
    def build(self, *, engine: "Engine", **kwargs) -> Level:
        level = Level(width=self.width, height=self.height)
        # self.builder.build(level)
        for i in range(5000):
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
                actionPoints=100
            )
            level.addEntity(test_monster)

        return level
