from genie.script.action import Action

class PlayerTimerAction(Action):
    def __init__(self, priority):
        self._FALLSPEED_RESET_RESET = 120
        self._DOUNUT_RESET = 30
        self._fallspeed_reset_timer = self._FALLSPEED_RESET_RESET
        self._dounut_timer = self._DOUNUT_RESET
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        if player.get_max_fallspeed() < player.get_max_fallspeed_reset_to():
            self._fallspeed_reset_timer -= 1
            if self._fallspeed_reset_timer <= 0:
                self._fallspeed_reset_timer = self._FALLSPEED_RESET_RESET
                player.set_max_fallspeed(player.get_max_fallspeed_reset_to())

        if not player.get_can_throw_dounut():
            self._dounut_timer -= 1
            if self._dounut_timer <= 0:
                self._dounut_timer = self._DOUNUT_RESET
                player.set_can_throw_dounut(True)