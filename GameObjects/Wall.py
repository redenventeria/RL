from GameObjects.GameObject import GameObject

class Wall(GameObject):
    def __init__(self):
        super().__init__(True, '#')