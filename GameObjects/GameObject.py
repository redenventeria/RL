from typing import Optional

class GameObject():
    def __init__(
        self, is_solid: bool,
        tile: str = '32',
        bg: Optional[tuple[int, int, int]] = (0, 0, 0),
        fg: Optional[tuple[int, int, int]] = (100, 100, 180),
    ):
        self.is_solid = is_solid
        self.tile = tile
        self.bg = bg
        self.fg = fg
