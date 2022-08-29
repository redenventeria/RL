from ctypes.wintypes import HPALETTE
from typing import TYPE_CHECKING, Optional

from ai import AI
if TYPE_CHECKING:
    from engine import Engine


class Entity:
    def __init__( self,
        *,
        is_solid: bool,
        is_blocking_fov: bool = False,
        char: str = '32',
        bg: Optional[tuple] = (0, 0, 0),
        fg: Optional[tuple] = (180, 180, 180),
        x: int,
        y: int,
        priority: int = 0,
        **kwargs
    ):
        self.is_solid = is_solid
        self.is_blocking_fov = is_blocking_fov
        self.tile = char
        self.bg = bg
        self.fg = fg
        self.x = x
        self.y = y
        self.priority = priority
    
    def getChar(self):
        return (self.tile, self.fg, self.bg)



class Empty(Entity):
    
    def __init__(self, *, x, y, **kwargs) -> None:
        super().__init__(is_solid=False, char='.', x=x, y=y)

    if TYPE_CHECKING:
        def append(self, entity):
            raise NotImplementedError()
class Wall(Entity):
    def __init__(self, *, x: int, y: int, bg=None, fg=None, char: str = "#", **kwargs):
        super().__init__(is_solid=True, char=char, x=x, y=y, bg=bg, fg=fg)


class PlayerEntity(Entity):

    def __init__(self, *, x, y, hp = 30, attack = 6, **kwargs):
        super().__init__(is_solid=True, char="@", x=x, y=y)
        self.hp = hp
        self.attack = attack



class AIEntity(Entity):

    def __init__(self, *,
        engine: "Engine",
        x: int,
        y: int,
        ai: AI,
        actionPoints: int,
        hp: int,
        attack: int,
        **kwargs
    ):
        super().__init__(x=x, y=y, **kwargs)
        self.ai = ai
        engine.AIEntities.add(self)