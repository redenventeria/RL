import tcod
import numpy
from GameObjects.Empty import Empty

class Game():
    def __init__(self, width: int, height: int, console: tcod.console.Console) -> None:
        self.width = width
        self.height = height
        self.console = console
        self.gameFieldWidth = 30
        self.gameFieldHeight = 30

        self.console.clear()

        self.game_field = [[Empty()]*self.gameFieldWidth for i in range(self.gameFieldHeight)]

        self.screen = numpy.zeros(
            shape=(height, width),
            dtype=tcod.console.Console.DTYPE,
            order="F"
        )

    def draw(self):
        self.console.clear()

        for i in range(self.gameFieldHeight):
            for j in range(self.gameFieldWidth):
                self.console.print(0, 0, "A")
                """ self.screen["ch"][i][j] = ord("_")
                self.screen["fg"][i][j] = (0, 0, 0, 0)
                self.screen["fg"][i][j] = (0, 0, 0, 0)"""
                #self.screen[i][j] = self.game_field[i][j].getTile()
        print(self.console)

g = Game(30, 30, tcod.console.Console(30, 30))
g.draw()