
from entity import Entity
from level import Level
from prefab_builder import BoxBuilder

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
    
    def build(self, **kwargs) -> Level:
        level = Level(width=self.width, height=self.height)
        # self.builder.build(level)

        test_monster = Entity(
            is_solid=True,
            is_blocking_fov=False,
            char="M",
            fg=(30, 230, 20),
            x=12,
            y=11,
            priority=10
        )

        level.addEntity(test_monster)

        return level
