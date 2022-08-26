from typing import TYPE_CHECKING, Optional

class Entity():
    def __init__( self,
        *,
        is_solid: bool,
        is_blocking_fov: bool = False,
        char: str = '32',
        bg: Optional[tuple] = (0, 0, 0),
        fg: Optional[tuple] = (180, 180, 180),
        x: int,
        y: int,
    ):
        self.is_solid = is_solid
        self.is_blocking_fov = is_blocking_fov
        self.tile = char
        self.bg = bg
        self.fg = fg
        self.x = x
        self.y = y



class Empty(Entity):
    
    def __init__(self, *, x, y) -> None:
        super().__init__(is_solid=False, char='.', x=x, y=y)

    if TYPE_CHECKING:
        def append(self, entity):
            raise NotImplementedError()



class Item(Entity):
    
    def __init__(self):
        pass



class Wall(Entity):
    def __init__(self, *, x: int, y: int):
        super().__init__(is_solid=True, char='#', x=x, y=y)