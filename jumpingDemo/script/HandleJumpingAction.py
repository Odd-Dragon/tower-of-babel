from genie.script.action import Action
from genie.services import *
GRAVITY = 1

class HandleJumpingAction(Action):
    def __init__(self, priority, keyboard_service):
        self._keyboard_service = keyboard_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        if self._keyboard_service.is_key_pressed(keys.SPACE) and not player.get_airborne():
            player.set_airborne(True)
            player.set_vy(-20)