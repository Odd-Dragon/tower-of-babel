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

        PLAYERSPEED = 5
        AIRDRAG = 0.5
        do_airdrag = True

        #if not self._keyboard_service.is_key_down(keys.A) and not self._keyboard_service.is_key_down(keys.D):
        if do_airdrag:
            if player_vx < AIRDRAG and player_vx > -AIRDRAG:
                player_vx = 0
            if player_vx > 0:
                player_vx -= AIRDRAG
                if player_vx > AIRDRAG*10:
                    player_vx -= AIRDRAG

            if player_vx < 0:
                player_vx += AIRDRAG
                if player_vx < AIRDRAG*-10:
                    player_vx += AIRDRAG

        if self._keyboard_service.is_key_down(keys.A):
            if player.get_vx() > -PLAYERSPEED:
                player_vx = -PLAYERSPEED
        if self._keyboard_service.is_key_down(keys.D):
            if player.get_vx() < PLAYERSPEED:
                player_vx = PLAYERSPEED
        
        
                

        player.set_vx(player_vx)
