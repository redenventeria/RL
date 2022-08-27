from tcod.event import (
    EventDispatch,
    KeyDown, Quit,
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    wait
)

from action_handler import (
    Action, ActionHandler, MovementAction, EscapeAction
)

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from engine import Engine

class tcodEventReceiver:
    def __init__(self, engine: "Engine", actionHandler: ActionHandler):
        self.actionHandler = actionHandler
        self.eventHandler = tcodEventHandler()
        self.engine = engine
    
    def getEvents(self):
        return wait()
            

    
    def handleEvent(self, event):
        return self.eventHandler.dispatch(event)

class tcodEventHandler(EventDispatch[Action]):

    def ev_quit(self, event: Quit) -> Optional[Action]:
        return EscapeAction()
    
    def ev_keydown(self, event: KeyDown) -> Optional[Action]:

        action: Optional[Action] = None

        key = event.sym

        actions: dict[int, tuple[int, int]] = {
            K_DOWN : (0, 1),
            K_UP : (0, -1),
            K_LEFT : (-1, 0),
            K_RIGHT : (1, 0),
        }

        if key in actions:
            action = MovementAction(*actions[key])
        
        return action

