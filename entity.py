from typing import TYPE_CHECKING, Optional


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
        priority: int = 0
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
        return (self.tile, self.bg, self.fg)



class Empty(Entity):
    
    def __init__(self, *, x, y) -> None:
        super().__init__(is_solid=False, char='.', x=x, y=y)

    if TYPE_CHECKING:
        def append(self, entity):
            raise NotImplementedError()
class Wall(Entity):
    def __init__(self, *, x: int, y: int, bg=None, fg=None, char: str = "#"):
        super().__init__(is_solid=True, char=char, x=x, y=y, bg=bg, fg=fg)