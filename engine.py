from typing import Set
from tcod_event_handler import tcodEventReceiver
from action_handler import ActionHandler
from entity import AIEntity, Empty, PlayerEntity
from level_builder import BSPLevelBuilder
from tcod_render import tcodRender
from time_flow import TimeFlow
from util import Tile, Vector2D


class Engine():
    def __init__(self) -> None:
        self.dimensions = Vector2D(60, 45)

        self.player = PlayerEntity(Tile("@", None, None), Vector2D(30, 30))

        self.AIEntities: Set[AIEntity] = set()

        self.actionHandler = ActionHandler(self)
        self.eventHandler = tcodEventReceiver(self, self.actionHandler)

        self.initialLevelBuilder = BSPLevelBuilder(self.dimensions)
        self.currentLevel = self.initialLevelBuilder.build(engine=self)

        #TODO Delegate player placement code to level builders

        for x in range(self.currentLevel.limits.dimensions.x):
            for y in range(self.currentLevel.limits.dimensions.y):
                if isinstance(self.currentLevel.entities[x, y], Empty):
                    self.player.position = Vector2D(x, y)
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
                        if action.APCost > 0:
                            self.isPlayerTurn = False
            self.timeFlow.makeAITurns()
