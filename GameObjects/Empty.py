from GameObjects.GameObject import GameObject

class Empty(GameObject):
    
    def __init__(self) -> None:
        super().__init__()
        self.tile = ord('_')
        self.bg = (0, 0, 0, 1)
        self.fg = (1, 1, 1, 1)