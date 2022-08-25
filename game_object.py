from typing import Optional

class GameObject():
    def __init__(
        self, is_solid: bool,
        tile: str = '32',
        bg: Optional[tuple] = (0, 0, 0),
        fg: Optional[tuple] = (100, 100, 180),
    ):
        self.is_solid = is_solid
        self.tile = tile
        self.bg = bg
        self.fg = fg



class Empty(GameObject):
    
    def __init__(self) -> None:
        super().__init__(False, '.')



class Item(GameObject):
    
    def __init__(self):
        pass



class Wall(GameObject):
    def __init__(self):
        super().__init__(True, '#')