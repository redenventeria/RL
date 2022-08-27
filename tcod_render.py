# TODO: Move all drawing code in this file

from typing import TYPE_CHECKING, Tuple
from tcod import Console
from tcod.context import Context

if TYPE_CHECKING:
    from engine import Engine

class tcodRender:

    def __init__(self,
        context: Context,
        console: Console,
        engine: "Engine",
        render_pos: Tuple[int, int] = (0, 0),
    ):
        self.context = context
        self.console = console
        self.engine = engine
        self.render_pos = render_pos
        pass

    def draw(self) -> None:
        for x in range(self.engine.width):
            for y in range(self.engine.height):
                tile, fg, bg = self.engine.currentLevel.getTile(x, y)
                self.console.print(
                    x + self.render_pos[0],
                    y + self.render_pos[1],
                    tile, fg=fg, bg=bg
                )
        
        self.context.present(self.console)
