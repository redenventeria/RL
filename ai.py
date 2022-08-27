
from action_handler import IdleAction, MovementAction
import random


class AI:
    def __init__(self, **kwargs):
        pass

    def getAction(self, **kwargs):
        pass

class IdleAI(AI):
    def __init__(self, **kwargs):
        pass

    def getAction(self, **kwargs):
        return None

class randomAI(AI):
    def __init__(self, **kwargs):
        pass

    def getAction(self, **kwargs):
        direction = random.choice([(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)])
        return MovementAction(*direction)
