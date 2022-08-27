from pydoc import plain
from typing import Set
from tcod_event_handler import tcodEventReceiver
from action_handler import ActionHandler
from entity import AIEntity, PlayerEntity
from level_builder import TestingBox
from tcod_render import tcodRender
from timeflow import TimeFlow


class Engine():
    def __init__(self) -> None:
        self.width = 60
        self.height = 45

        self.player = PlayerEntity(is_solid=True, char="@", x=44, y=30)

        self.AIEntities: Set[AIEntity] = set()

        self.actionHandler = ActionHandler(self)
        self.eventHandler = tcodEventReceiver(self, self.actionHandler)

        self.initialLevelBuilder = TestingBox(width=self.width, height=self.height)
        self.currentLevel = self.initialLevelBuilder.build(engine=self)
        self.currentLevel.addEntity(self.player)

        self.timeFlow = TimeFlow(self)
    
    def setRender(self, render: tcodRender):
        self.render = render
    
    def mainloop(self):
        while True:
            self.isPlayerTurn = True
            while self.isPlayerTurn == True:
                self.render.draw()
                events = self.eventHandler.getEvents()
                for event in events:
                    action = self.eventHandler.handleEvent(event)
                    if action != None:
                        action.apply(engine=self, entity=self.player)
                        self.isPlayerTurn = False
            self.timeFlow.makeAITurns()