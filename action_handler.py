
from typing import TYPE_CHECKING

from entity import Entity
from level import Level


if TYPE_CHECKING:
    from engine import Engine


class Action:

    def __init__(self):
        pass

    def apply(self, **kwargs):
        pass

    

class MovementAction(Action):
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()
        self.dx: int = dx
        self.dy: int = dy
    
    def apply(self, **kwargs):

        level = kwargs["level"]
        entity = kwargs["entity"]

        new_x = entity.x + self.dx
        new_y = entity.y + self.dy
        level.moveEntity(entity, new_x, new_y)


class EscapeAction(Action):

    def __init__(self) -> None:
        super().__init__()
    
    def apply(self, **kwargs):
        raise SystemExit()



class ActionHandler:

    def __init__(self, game):
        self.game = game
    
    def apply(self, action: Action, **kwargs):
        if action != None:
            action.apply(**kwargs)