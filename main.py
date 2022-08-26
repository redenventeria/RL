#!/usr/bin/env python3

from typing import Optional, Any

from tcod.tileset import load_tilesheet, Tileset, CHARMAP_CP437
from tcod.event import wait
from tcod import Console
from tcod.context import new as new_context

from engine import Engine

def main() -> None:

    WIDTH, HEIGHT = 60, 45

    tileset: Tileset = load_tilesheet(
        "resources/Alloy_curses_12x12.png", 16, 16, CHARMAP_CP437,
    )

    engine = Engine(Console(WIDTH, HEIGHT))

    with new_context(
        columns=WIDTH,
        rows=HEIGHT,
        tileset=tileset
    ) as context:
        while True:
            
            engine.draw()

            context.present(engine.console)

            for event in wait():
                context.convert_event(event)
                print(event)
                action: Optional[Any] = engine.eventHandler.dispatch(event)
                engine.actionHandler.apply(action, entity=engine.player, level=engine.current_level)

if __name__ == "__main__":
    main()