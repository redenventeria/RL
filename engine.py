import random
from tcod.console import Console
from event_handler import EventHandler
from action_handler import ActionHandler
from entity import Entity
from level import Level
from prefab_builder import BoxBuilder
from level_builder import TestingBox
from tcod_render import tcodRender


class Engine():
    def __init__(self) -> None:
        self.width = 60
        self.height = 45

        self.player = Entity(is_solid=True, char="@", x=44, y=30)

        self.eventHandler = EventHandler()
        self.actionHandler = ActionHandler(self)

        self.initialLevelBuilder = TestingBox(width=self.width, height=self.height)
        self.currentLevel = self.initialLevelBuilder.build()
        self.currentLevel.addEntity(self.player)

    def handleEvent(self, event):
        action = self.eventHandler.dispatch(event)
        self.actionHandler.apply(action, entity=self.player, level=self.currentLevel)
    
    def setRender(self, render: tcodRender):
        self.render = render
    
    def display(self):
        self.render.draw()