from util import Vector2D, Rectangle
import numpy as np
from math import sqrt
from queue import PriorityQueue

INACTIVE_CELL = 0
CALCULATED_CELL = 1
VISITED_CELL = 2

TOTAL_DISTANCE = 3

PathCell = np.dtype([
    ("visited", np.uint8),
    ("startDistance", np.uint32),
    ("targetDistance", np.uint32),
    ("totalDistance", np.uint32),
    ("ParentX", np.uint32),
    ("ParentY", np.uint32),
])

DefaultCell = (INACTIVE_CELL, 0, 0, 0, 0, 0)

def StepsMetric(a:Vector2D, b: Vector2D):
    diag_count = min(abs(a.x - b.x), abs(a.y - b.y))
    straight_vount = max(abs(a.x - b.x), abs(a.y - b.y)) - diag_count
    return diag_count * 14 + straight_vount * 10

def EuclideanMetric(a: Vector2D, b: Vector2D):
    return round(sqrt((b.x - a.x)**2 + (b.y - a.y)**2), 1) * 10

# TODO Clean up file, finish developing A* algorithm (right now it is a mess).
class PathfindingEnviroment:

    def __init__(self, enviroment: np.ndarray, accessibility: np.ndarray):
        """enviroment cells store single value: weight of going through a cell."""
        self.enviroment = np.copy(enviroment)
        self.isAccessible = np.copy(accessibility)
    
    def findPath(self, startPos: Vector2D, targetPos: Vector2D):

        # Looking for a path:

        env = self.enviroment
        envMap = np.zeros(env.shape, dtype=PathCell)
        envMap.fill(DefaultCell)
        cellQueue = PriorityQueue()


        currentCellPos: Vector2D = startPos

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

        envMap[startPos.asTuple()] = CALCULATED_CELL

        startCell = envMap[startPos.asTuple()] = self.calculateEnvCell(
            startPos,
            startPos,
            startPos,
            targetPos,
            envMap
        )

        cellQueue.put((startCell[TOTAL_DISTANCE], startPos))

        while(envMap[currentCellPos.asTuple()]["targetDistance"] > 0 and not cellQueue.empty()):
            currentCellPos = cellQueue.get_nowait()[1]
            print(currentCellPos.asTuple())

            for cellShift in surroundingCells:

                newPos = currentCellPos + cellShift

                if Rectangle(
                    Vector2D(0, 0),
                    Vector2D.fromIterable(envMap.shape)
                ).contains(newPos) and self.isAccessible[newPos.asTuple()]:

                    if envMap[newPos[0]][newPos[1]]["visited"] == INACTIVE_CELL:
                        envMap[newPos[0]][newPos[1]] = self.calculateEnvCell(
                            newPos,
                            currentCellPos,
                            startPos,
                            targetPos,
                            envMap
                        )
                        cellQueue.put_nowait((
                            envMap[newPos[0]][newPos[1]]["startDistance"] + envMap[newPos[0]][newPos[1]]["targetDistance"],
                             newPos
                             )
                        )

            envMap[currentCellPos.asTuple()]["visited"] = VISITED_CELL

        if envMap[currentCellPos.asTuple()]["targetDistance"] != 0:
            raise NotImplementedError
        
        print("Finish!")

        # Restoring a path:

        path = []

        currentCellPos = targetPos

        while currentCellPos != startPos:

            path.append(currentCellPos)

            minTotalDistance = 999999
            closestCell = 0

            for cellShift in surroundingCells:
                
                newPos = currentCellPos + cellShift

                if Rectangle(
                    Vector2D(0, 0),
                    Vector2D.fromIterable(envMap.shape)
                ).contains(newPos) and self.isAccessible[newPos.asTuple()]:
                    if envMap[newPos.asTuple()]["totalDistance"] < minTotalDistance:
                        minTotalDistance = envMap[newPos.asTuple()]["totalDistance"]
                        closestCell = newPos
                
            currentCellPos = closestCell
        
        path.append(startPos)
        path.reverse()

        return path

                

    def calculateEnvCell(
        self,
        cellPos: Vector2D,
        prevPos: Vector2D,
        startPos: Vector2D,
        targetPos: Vector2D,
        envMap
        ):

        toStart = StepsMetric(cellPos, startPos)
        toTarget = StepsMetric(cellPos, targetPos)

        return (
            CALCULATED_CELL,
            toStart,
            toTarget,
            envMap[prevPos.asTuple()]["totalDistance"] + StepsMetric(cellPos, prevPos) * self.enviroment[cellPos.asTuple()],
            prevPos.x,
            prevPos.y
        )



shape = (10, 10)
area = np.ones(shape)
walls = np.ones(shape)

walls[1][1:3] = 0
walls[2][1:5] = 0
walls[3][1:5] = 0
walls[4][1:5] = 0
walls[5][1:10] = 0


path = PathfindingEnviroment(area, walls)

answer = path.findPath(Vector2D(0, 9), Vector2D(9, 0))

graph = np.ones(shape)

for elem in answer:
    graph[elem.asTuple()] = 0.5

for i in range(shape[0]):
    for j in range(shape[1]):
        if not walls[i][j]:
            graph[i][j] = 0

from matplotlib import pyplot as plt
import matplotlib.cm as cm

plt.imshow(graph, cmap=cm.gray)
plt.show()




        



