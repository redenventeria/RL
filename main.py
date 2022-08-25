#!/usr/bin/env python3

from typing import Optional, Any
from tcod.tileset import load_tilesheet, Tileset, CHARMAP_CP437
from tcod.event import wait, Quit
from tcod import Console
from tcod.context import Context, new as new_context

from game import Game

def main() -> None:

    WIDTH, HEIGHT = 45, 45

    tileset: Tileset = load_tilesheet(
        "Alloy_curses_12x12.png", 16, 16, CHARMAP_CP437,
    )

    game = Game(WIDTH, HEIGHT)

    with new_context(
        columns=WIDTH,
        rows=HEIGHT,
        tileset=tileset
    ) as context:
        while True:
            
            game.draw()

            context.present(game.console)

            for event in wait():
                context.convert_event(event)

                print(event)

                action: Optional[Any] = game.eventHandler.dispatch(event)
                game.actionHandler.apply(action)

if __name__ == "__main__":
    main()