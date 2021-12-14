from genie.script.action import Action
from genie.services import *
from jumpingDemo.cast.dounut import Dounut
GRAVITY = 0.4

class ThrowDounutAction(Action):
    def __init__(self, priority, keyboard_service, audio_service):
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")

        if self._keyboard_service.is_key_pressed(keys.SPACE) and player.get_can_throw_dounut():
            player.set_can_throw_dounut(False)
            THROWSPEED_X = 8
            THROWSPEED_Y = -6
            self._audio_service.play_sound("resources/dounut-throw.wav", 0.1)
            velocity_x = player.get_vx()
            if player.get_is_facing_right():
                velocity_x += THROWSPEED_X
            else:
                velocity_x -= THROWSPEED_X
                    
            velocity_y = player.get_vy() + THROWSPEED_Y

            new_dounut = Dounut("resources/dounut.png", 12, 12, player.get_x(), player.get_y(), velocity_x, velocity_y, 0, 10, False)
            actors.add_actor("dounuts", new_dounut)