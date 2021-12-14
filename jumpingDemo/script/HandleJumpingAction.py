from genie.script.action import Action
from genie.services import *

class HandleJumpingAction(Action):
    def __init__(self, priority, keyboard_service, audio_service):
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        JUMPSPEED = -9
        DASHSPEED_Y = -10
        DASHSPEED_X = 16
        player = actors.get_first_actor("player")
        
        if self._keyboard_service.is_key_pressed(keys.W) and not player.get_airborne():
            player.set_airborne(True)
            player.set_vy(JUMPSPEED)
            self._audio_service.play_sound("resources/jump.wav", 0.1)

        if self._keyboard_service.is_key_pressed(keys.E) and player.get_feathers() > 0:
            player.remove_a_feather()
            actors.remove_actor("feather_display", actors.get_last_actor("feather_display"))
            player.set_max_fallspeed(2)
            if player.get_vy() > DASHSPEED_Y and player.get_airborne():
                player.set_vy(DASHSPEED_Y)
            if player.get_vx() > 0:
                player.set_vx(player.get_vx()+DASHSPEED_X)
                #player.set_x(player.get_x()+DASHSPEED_X*2)
            if player.get_vx() < 0:
                player.set_vx(player.get_vx()-DASHSPEED_X)
                #player.set_x(player.get_x()-DASHSPEED_X*2)
            self._audio_service.play_sound("resources/zombie-dash.wav", 0.1)