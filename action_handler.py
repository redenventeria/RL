
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from entity import Entity


if TYPE_CHECKING:
    from engine import Engine


class Action:

    def __init__(self, **kwargs):
        pass

    def apply(self, engine, entity, **kwargs):
        pass

class IdleAction(Action):
    def __init__(self, **kwargs):
        pass

    def apply(self, engine, entity, **kwargs):
        pass
    

class MovementAction(Action):
    def __init__(self, dx: int, dy: int, **kwargs) -> None:
        super().__init__()
        self.dx: int = dx
        self.dy: int = dy
    
    def apply(self, *, engine: "Engine", entity: "Entity", **kwargs):

        new_x = entity.x + self.dx
        new_y = entity.y + self.dy
        engine.currentLevel.moveEntity(entity, new_x, new_y)


class EscapeAction(Action):

    def __init__(self, **kwargs) -> None:
        super().__init__()
    
    def apply(self, **kwargs):
        raise SystemExit()



class ActionHandler:

    def __init__(self, game):
        self.game = game
    
    def apply(self, action: Action, **kwargs):
        if action != None:
            action.apply(**kwargs)