from genie.script.action import Action
from globals import *
class MoveBackgroundAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, cast, actions, clock, callback):
        backgrounds = cast.get_actors("background")
        for background in backgrounds:
            if background.get_y() > W_SIZE[1]*1.1:
                background.set_y(W_SIZE[1]*-0.1)
            