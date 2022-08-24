class ActionHandler:

    def __init__(self, game):
        self.game = game
    
    def apply(self, action):
        if action != None:
            action.apply(self.game)