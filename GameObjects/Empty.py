from GameObjects.GameObject import GameObject
from typing import Optional

class Empty(GameObject):
    
    def __init__(self) -> None:
        super().__init__(False, '.')