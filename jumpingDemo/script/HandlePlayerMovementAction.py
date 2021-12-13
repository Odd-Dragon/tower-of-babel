from genie.script.action import InputAction
from genie.services import *
GRAVITY = 1

class HandlePlayerMovementAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
        
        
    def execute(self, actors, actions, clock, callback):
        self.player = actors.get_first_actor("player")
        player_vx = self.player.get_vx()

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
            self.player.set_animating(True)
            if not self.player.flipped():
                self.player.flip_image()
            if self.player.get_vx() > -PLAYERSPEED:
                player_vx = -PLAYERSPEED
                self.player.set_is_facing_right(False)
                
        if self._keyboard_service.is_key_down(keys.D):
            self.player.set_animating(True)
            if  self.player.flipped():
                self.player.flip_image()
            if self.player.get_vx() < PLAYERSPEED:
                player_vx = PLAYERSPEED
                self.player.set_is_facing_right(True)
                
        
        
                

        self.player.set_vx(player_vx)
