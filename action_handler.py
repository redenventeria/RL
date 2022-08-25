


class Action:

    def apply(self):
        pass

    

class MovementAction(Action):
    def __init__(self, dx: int, dy: int) -> None:
        super().__init__()
        self.dx: int = dx
        self.dy: int = dy
    
    def apply(self, game):
        new_x = game.player_x + self.dx
        new_y = game.player_y + self.dy
        if not game.level[new_x][new_y].is_solid:
            game.player_x = new_x
            game.player_y = new_y



class EscapeAction(Action):

    def __init__(self) -> None:
        super().__init__()
    
    def apply(self, game):
        raise SystemExit()



class ActionHandler:

    def __init__(self, game):
        self.game = game
    
    def apply(self, action):
        if action != None:
            action.apply(self.game)