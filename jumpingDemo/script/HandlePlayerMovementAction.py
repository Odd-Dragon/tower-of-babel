from genie.script.action import Action
from genie.services import *
GRAVITY = 1

class HandlePlayerMovementAction(Action):
    def __init__(self, priority, keyboard_service):
        self._keyboard_service = keyboard_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")

        player_vx = player.get_vx()

        if self._keyboard_service.is_key_down(keys.LEFT):
            player_vx = -7
        if self._keyboard_service.is_key_down(keys.RIGHT):
            player_vx = 7
        
        if not self._keyboard_service.is_key_down(keys.LEFT) and not self._keyboard_service.is_key_down(keys.RIGHT):
            if player_vx > 0:
                player_vx -= 1
            if player_vx < 0:
                player_vx += 1

        player.set_vx(player_vx)
