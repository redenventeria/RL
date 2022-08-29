import numpy as np
from entity import Empty, Entity
from typing import List, Tuple, TypeVar, Union

from util import Rectangle, Vector2D

Cell = np.dtype([
    ("solid", np.bool8),
    ("blocking_fov", np.bool8),
    ("lit", np.bool8),
])

EntityList = Union[Empty, List[Entity]]

class Level:

    def __init__(self, dimensions: Vector2D):

        self.limits = Rectangle(Vector2D(0, 0), dimensions)

        self.entities: dict[Vector2D, EntityList] = {}
        dimensions = self.limits.dimensions
        for x in range(dimensions.x):
            for y in range(dimensions.y):
                position = Vector2D(x, y)
                self.entities[position] = Empty(position)

        self.navGrid = np.full(
            dimensions,
            fill_value=False,
            dtype=Cell,
        )
    
    def updateNavCell(self, position: Vector2D):

        cell = self.navGrid[position[0], position[1]]

        if isinstance(self.entities[position], Empty):
            cell["solid"] = False
            cell["blocking_fov"] = False
        else:
            cell["solid"] = False
            cell["blocking_fov"] = False
            for e in self.entities[position]:
                cell["solid"] = cell["solid"] or e.is_solid
                cell["blocking_fov"] = cell["blocking_fov"] or e.is_blocking_fov
    
    def addEntity(self, entity: Entity):
        position = entity.position
        if isinstance(entity, Empty):
            self.entities[position] = entity
        else:
            print(type(position))
            if isinstance(self.entities[position], Empty):
                self.entities[position] = [entity]
            else:
                self.entities[position].append(entity)
        
        self.updateNavCell(position.asTuple())
    
    def deleteEntity(self, entity: Entity):
        position = entity.position
        instance_index: int
        for i, e in enumerate(self.entities[position]):
            if e is entity:
                instance_index = i
        del self.entities[position][instance_index]

        if len(self.entities[position]) == 0:
            self.entities[position] = Empty(position)
        
        self.updateNavCell(position)
    
    def moveEntity(self, entity: Entity, newPosition: Tuple[int, int]):
        if self.limits.contains(newPosition):
            if not self.navGrid[newPosition[0], newPosition[1]]["solid"]:
                self.deleteEntity(entity)

                entity.position = newPosition

                self.addEntity(entity)
        
    
    def getTile(self, position):
        entities = self.entities[position]
        if isinstance(entities, Empty):
            return entities.getTile()
        else:
            most_important_entity = entities[0]
            for e in entities:
                if e.priority > most_important_entity.priority:
                    most_important_entity = e
            return most_important_entity.getTile()



