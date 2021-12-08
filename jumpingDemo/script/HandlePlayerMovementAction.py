from genie.script.action import Action
from genie.services import *
GRAVITY = 1

class HandlePlayerMovementAction(Action):
    def __init__(self, priority, keyboard_service):
        self._keyboard_service = keyboard_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        if self._keyboard_service.is_key_down(keys.LEFT):
            player.set_vx(-3)
        if self._keyboard_service.is_key_down(keys.RIGHT):
            player.set_vx(3)
        
        if not self._keyboard_service.is_key_down(keys.LEFT) and not self._keyboard_service.is_key_down(keys.RIGHT):
            player.set_vx(0)