from IsSolid import IsSolid
from GameObject import GameObject

class Wall(GameObject, IsSolid):
    def __init__(self):

        super().__init__(True)
        self.tile = chr(178)