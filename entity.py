
from typing import TYPE_CHECKING, Optional

from ai import AI
from util import Tile, Vector2D
if TYPE_CHECKING:
    from engine import Engine


class Entity:
    def __init__( self,
        position: Vector2D,
        tile: Tile,
        is_solid: bool,
        is_blocking_fov: bool,
        priority: int = 0,
    ):
        self.tile = tile
        self.position = position
        self.is_solid = is_solid
        self.is_blocking_fov = is_blocking_fov
        self.priority = priority
    
    def getTile(self):
        return self.tile



class Empty(Entity):
    
    def __init__(self, position: Vector2D, *args) -> None:
        super().__init__(position, Tile(".", None, None), False, False *args)

    if TYPE_CHECKING:
        def append(self, entity):
            raise NotImplementedError()

class Wall(Entity):
    def __init__(self,
        position: Vector2D,
        tile: Tile = Tile("#", None, None),
        is_solid=True,
        is_blocking_fov = True,
        **kwargs
    ):
        super().__init__(position, tile, is_solid, is_blocking_fov)


class PlayerEntity(Entity):

    def __init__(self, tile: Tile, position: Vector2D, *args, hp = 30, attack = 6):
        super().__init__(position, tile, True, False)
        self.hp = hp
        self.attack = attack



class AIEntity(Entity):

    def __init__(self, *,
        engine: "Engine",
        position: Vector2D,
        tile: Tile,
        ai: AI,
        actionPoints: int,
        hp: int,
        attack: int,
        **kwargs
    ):
        super().__init__(position=position, **kwargs)
        self.ai = ai
        engine.AIEntities.add(self)