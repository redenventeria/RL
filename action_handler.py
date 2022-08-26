
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from engine import Engine


class Action:

    def apply(self):
        pass

    

class MovementAction(Action):
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()
        self.dx: int = dx
        self.dy: int = dy
    
    def apply(self, engine: "Engine"):
        new_x = engine.player.x + self.dx
        new_y = engine.player.y + self.dy
        if self.__isCellExists(new_x, new_y, engine):
            if not engine.current_level.navGrid[new_x][new_y].is_solid:
                engine.player.x = new_x
                engine.player.y = new_y
    
    def __isCellExists(self, new_x, new_y, engine: "Engine"):
        return 0 <= new_x < engine.width and 0 <= new_y < engine.height


class EscapeAction(Action):

    def __init__(self) -> None:
        super().__init__()
    
    def apply(self, engine: "Engine"):
        raise SystemExit()



class ActionHandler:

    def __init__(self, game):
        self.game = game
    
    def apply(self, action):
        if action != None:
            action.apply(self.game)