from util import Vector2D, Rectangle
import numpy as np
from math import sqrt
from queue import PriorityQueue

INACTIVE_CELL = 0
CALCULATED_CELL = 1
VISITED_CELL = 2

PathCell = np.dtype([
    ("visited", np.uint32),
    ("startDistance", np.uint32),
    ("targetDistance", np.uint32),
    ("totalDistance", np.uint32),
    ("ParentX", np.uint32),
    ("ParentY", np.uint32),
])

DefaultCell = (INACTIVE_CELL, 0, 0, 0, 0, 0)

def EuclideanMetric(a: Vector2D, b: Vector2D):
    return round(sqrt((b.x - a.x)**2 + (b.y - a.y)**2) * 10)

class PathfindingEnviroment:

    def __init__(self, enviroment: np.ndarray):
        """enviroment cells store single value: weight of going through a cell."""
        self.enviroment = np.copy(enviroment)
    
    def findPath(self, startPos: Vector2D, targetPos: Vector2D):

        env = self.enviroment
        envMap = np.zeros(env.shape, dtype=PathCell)
        envMap.fill(DefaultCell)
        cellQueue = PriorityQueue()

        currentCellPos: Vector2D = startPos

        dist = EuclideanMetric(startPos, targetPos),

        envMap[startPos.asTuple()] =  CALCULATED_CELL
        print(envMap)
        while(envMap[currentCellPos.asTuple()]["targetDistance"] != 0):
            surroundingCells = [
                Vector2D(0, 1),
                Vector2D(1, 0),
                Vector2D(0, -1),
                Vector2D(-1, 0),
                Vector2D(-1, -1),
                Vector2D(-1, 1),
                Vector2D(1, -1),
                Vector2D(1, 1),
            ]

            for cellPos in surroundingCells:
                if Rectangle(
                    Vector2D(0, 0),
                    Vector2D.fromIterable(envMap.shape)
                    ).contains(cellPos):
                    
                    if envMap[cellPos]["visited"] == INACTIVE_CELL or \
                    envMap[cellPos]["totalPathWeight"] < envMap[currentCellPos]["totalPathWeight"]:
                        envMap[cellPos] = self.calculateEnvCell(
                            cellPos,
                            currentCellPos,
                            startPos,
                            targetPos
                        )

    def calculateEnvCell(
        self,
        cellPos: Vector2D,
        prevPos: Vector2D,
        startPos: Vector2D,
        targetPos: Vector2D,
        ) -> PathCell:

        toStart = EuclideanMetric(cellPos, startPos)
        toTarget = EuclideanMetric(cellPos, targetPos)

        return (
            CALCULATED_CELL,
            toStart,
            toTarget,
            (toStart + toTarget) * self.enviroment[cellPos],
            prevPos
        )

area = np.ones((10, 10))

path = PathfindingEnviroment(area)

path.findPath(Vector2D(0, 0), Vector2D(9, 9))

        



