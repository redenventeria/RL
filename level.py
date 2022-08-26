import numpy as np
from entity import Empty, Entity
from typing import List, Tuple, TypeVar, Union

Cell = np.dtype([
    ("solid", np.bool8),
    ("blocking_fov", np.bool8),
    ("lit", np.bool8),
])

EntityList = Union[Empty, List[Entity]]

class Level:

    def __init__(self, *, width, height):

        self.width = width
        self.height = height

        self.entities: dict[Tuple[int, int], EntityList]

        for x in range(self.width):
            for y in range(self.height):
                self.entities[(x, y)] = Empty(x=x, y=y)

        self.navGrid = np.full(
            (width, height),
            fill_value=(False, False, False),
            dtype=Cell
        )
    
    def add_entity(self, entity: Entity):
        cell = self.navGrid[entity.x][entity.y]
        cell["solid"] = cell["solid"] or entity.is_solid
        cell["blocking_fov"] = cell["blocking_fov"] or entity.is_blocking_fov
        if not isinstance(self.entities[(entity.x, entity.y)], Empty):
            self.entities[entity.x, entity.y] = [entity]
        else:
            self.entities[entity.x, entity.y].append(entity)


