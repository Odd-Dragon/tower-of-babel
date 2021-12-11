from genie.script.action import Action
from genie.services import *
from jumpingDemo.cast.dounut import Dounut
GRAVITY = 0.4

class ThrowDounutAction(Action):
    def __init__(self, priority, keyboard_service, audio_service):
        self._keyboard_service = keyboard_service
        self._TIMER_RESET = 60
        self._timer = self._TIMER_RESET
        self._audio_service = audio_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")

        if not player.get_can_throw_dounut and self._timer > 0:
            self._timer -= 1
        else:
            if not player.get_can_throw_dounut():
                player.set_can_throw_dounut(True)
                print("PLAYER CAN THROW DOUNUT. REPLACE THIS WITH A VISUAL INDICATOR.")
                self._timer = self._TIMER_RESET
        if self._keyboard_service.is_key_pressed(keys.SPACE):
            THROWSPEED_X = 8
            THROWSPEED_Y = -6
            self._audio_service.play_sound("genie/assets/dounut-throw.wav", 0.1)
            if player.get_can_throw_dounut():
                velocity_x = player.get_vx()
                if player.get_is_facing_right():
                    velocity_x += THROWSPEED_X
                else:
                    velocity_x -= THROWSPEED_X
                    
                velocity_y = player.get_vy() + THROWSPEED_Y

                new_dounut = Dounut("resources/dounut.png", 6, 6, player.get_x(), player.get_y(), velocity_x, velocity_y, 0, 10, False)
                actors.add_actor("dounuts", new_dounut)