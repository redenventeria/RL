#!/usr/bin/env python3

from typing import Optional, Any
from tcod.tileset import load_tilesheet, Tileset, CHARMAP_CP437
from tcod.event import wait
from tcod import Console
from tcod.context import new as new_context

from engine import Engine
from tcod_render import tcodRender
from util import Vector2D

def main() -> None:

    consoleDimensions = Vector2D(60, 45)

    tileset: Tileset = load_tilesheet(
        "resources/Alloy_curses_12x12.png", 16, 16, CHARMAP_CP437,
    )

    with new_context(
        columns=consoleDimensions.x,
        rows=consoleDimensions.y,
        tileset=tileset
    ) as context:

        console: Console = Console(consoleDimensions.x, consoleDimensions.y)
        engine = Engine()
        render = tcodRender(context, console, engine)
        
        engine.setRender(render)

        engine.mainloop()

if __name__ == "__main__":
    main()