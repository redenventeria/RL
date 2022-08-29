# TODO: Create a time system that will, based on speed, allow to
# track order of turns and applying of timed events.
# Begin with a simple system that will just make all AI entities and player take turns
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
            
