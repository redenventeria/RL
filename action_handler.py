
from typing import TYPE_CHECKING

from util import Vector2D
if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine


class Action:

    def __init__(self, **kwargs):
        self.APCost = 100
        pass

    def apply(self, engine, entity, **kwargs):
        pass

class IdleAction(Action):
    def __init__(self, **kwargs):
        self.APCost = 100
        pass

    def apply(self, engine, entity, **kwargs):
        pass
    

class MovementAction(Action):
    def __init__(self, direction: Vector2D, **kwargs) -> None:
        super().__init__()
        self.APCost = 100
        self.direction = direction
    
    def apply(self, *, engine: "Engine", entity: "Entity", **kwargs):

        newPosition = entity.position + self.direction
        engine.currentLevel.moveEntity(entity, newPosition)


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