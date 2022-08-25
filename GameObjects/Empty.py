from GameObjects import GameObject

class Empty(GameObject):
    
    def __init__(self) -> None:
        super().__init__(False, '.')