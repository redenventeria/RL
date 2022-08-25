from tcod.event import (
    EventDispatch,
    KeyDown, Quit,
    K_UP, K_DOWN, K_LEFT, K_RIGHT
)

from ActionHandler import (
    Action, MovementAction, EscapeAction
)

from typing import Optional

class EventHandler(EventDispatch[Action]):

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

