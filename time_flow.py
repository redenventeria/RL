from typing import TYPE_CHECKING, Union
from entity import PlayerEntity, AIEntity


if TYPE_CHECKING:
    from engine import Engine


class TimeFlow:

    def __init__(self, engine: "Engine") -> None:
        self.engine = engine
    
    def makeAITurns(self):
        for actor in self.engine.AIEntities:
            action = actor.ai.getAction()
            self.engine.actionHandler.apply(action, engine=self.engine, entity=actor)
            
