from genie.script.action import Action
from genie.services import *
GRAVITY = 0.5

class HandleJumpingAction(Action):
    def __init__(self, priority, keyboard_service):
        self._keyboard_service = keyboard_service
        self._TIMER_RESET = 200
        self._timer = self._TIMER_RESET
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        JUMPSPEED = -10
        DASHSPEED_Y = -8
        DASHSPEED_X = 15
        player = actors.get_first_actor("player")
        if self._timer > 0:
            self._timer -= 1
        else:
            if not player.get_has_dash():
                player.set_has_dash(True)
                print("PLAYER HAS DASH. REPLACE THIS WITH A VISUAL INDICATOR.")
                self._timer = self._TIMER_RESET
        
        if self._keyboard_service.is_key_pressed(keys.W) and not player.get_airborne():
            player.set_airborne(True)
            player.set_vy(JUMPSPEED)
        if self._keyboard_service.is_key_pressed(keys.E) and player.get_has_dash():
            player.set_has_dash(False)
            if player.get_vy() > DASHSPEED_Y and player.get_airborne():
                player.set_vy(DASHSPEED_Y)
            if player.get_vx() > 0:
                player.set_vx(player.get_vx()+DASHSPEED_X)
                #player.set_x(player.get_x()+DASHSPEED_X*2)
            if player.get_vx() < 0:
                player.set_vx(player.get_vx()-DASHSPEED_X)
                #player.set_x(player.get_x()-DASHSPEED_X*2)
        