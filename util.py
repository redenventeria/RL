from cmath import sqrt
from math import dist
from pathlib import Path
from typing import Iterable, Tuple
from random import randint
from queue import PriorityQueue
import numpy as np



class Vector2D:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    @classmethod
    def fromIterable(self, coordinates: Iterable):
        self.x, self.y = coordinates
    
    @classmethod
    def getRandom(self, xMin, xMax, yMin, yMax):
        return Vector2D(randint(xMin, xMax), randint(yMin, yMax))
    
    def asTuple(self):
        return (self.x, self.y)
    
    def __add__(self, other):

        try:
            return Vector2D(self.x + other.x, self.y + other.y)
        except AttributeError():
            raise TypeError()
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __floordiv__(self, other):
        return Vector2D(self.x // other, self.y // other)
    
    def __getitem__(self, index):
        return (self.x, self.y)[index]
    
    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == self.y
        except AttributeError:
            return self.x == other[0] and self.x == other[0] and len(other) == 2
    
    def __hash__(self):
        return (self.x, self.y).__hash__()




class Rectangle:

    def __init__(self, position: Vector2D, dimensions: Vector2D):
        self.position = position
        self.dimensions = dimensions

    @classmethod
    def fromInt(x: int, y: int, w: int, h: int):
        return Rectangle(Vector2D(x, y), Vector2D(w, h))
    
    def getOtherPoint(self):
        return Vector2D(
            self.position.x + self.dimensions.x,
            self.position.y + self.dimensions.y
        )
    
    def contains(self, position: Vector2D):
        x1, y1 = self.position
        x2, y2 = self.getOtherPoint()
        x, y = position
        return x1 <= x < x2 and y1 <= y < y2
    
    def __iter__(self):
        return iter(self.position, self.dimensions)



class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    @classmethod
    def fromIterable(self, iter: Iterable):
        self.r, self.g, self.b = iter
    
    def __iter__(self):
        return iter(self.r, self.g, self.b)



class Tile:

    def __init__(self, char: str, bg: Color, fg: Color):
        self.char = char
        self.bg = bg
        self.fg = fg
    
    def __iter__(self):
        yield self.char
        yield self.bg
        yield self.fg
