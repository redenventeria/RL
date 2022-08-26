from turtle import update
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

    def __init__(self, *, width: int, height: int):

        self.width = width
        self.height = height

        self.entities: dict[Tuple[int, int], EntityList] = {}

        for x in range(self.width):
            for y in range(self.height):
                self.entities[(x, y)] = Empty(x=x, y=y)

        self.navGrid = np.full(
            (width, height),
            fill_value=False,
            dtype=Cell,
        )
    
    def updateNavCell(self, x, y):

        cell = self.navGrid[x, y]

        if isinstance(self.entities[x, y], Empty):
            cell["solid"] = False
            cell["blocking_fov"] = False
        else:
            cell["solid"] = False
            cell["blocking_fov"] = False
            for e in self.entities[x, y]:
                cell["solid"] = cell["solid"] or e.is_solid
                cell["blocking_fov"] = cell["blocking_fov"] or e.is_blocking_fov
    
    def addEntity(self, entity: Entity):
        x = entity.x
        y = entity.y
        cell = self.navGrid[x][y]
        if isinstance(self.entities[x, y], Empty):
            self.entities[x, y] = [entity]
        else:
            self.entities[x, y].append(entity)
        
        self.updateNavCell(x, y)
    
    def deleteEntity(self, entity):
        x = entity.x
        y = entity.y
        instance_index: int
        for i, e in enumerate(self.entities[x, y]):
            if e is entity:
                instance_index = i
        del self.entities[x, y][instance_index]

        if len(self.entities[x, y]) == 0:
            self.entities[x, y] = Empty(x=x, y=y)
        
        self.updateNavCell(x, y)
    
    def moveEntity(self, entity: Entity, new_x, new_y):
        if self.__isCellExists(new_x, new_y):
            if not self.navGrid[new_x][new_y]["solid"]:
                self.deleteEntity(entity)

                entity.x = new_x
                entity.y = new_y

                self.addEntity(entity=entity)
        
    
    def getTile(self, x, y):
        entities = self.entities[x, y]
        if isinstance(entities, Empty):
            return entities.getChar()
        else:
            most_important_entity = entities[0]
            for e in entities:
                if e.priority > most_important_entity.priority:
                    most_important_entity = e
            return most_important_entity.getChar()
    
    def __isCellExists(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.height



