from genie.script.action import Action

class GameOver(Action):
    def __init__(self, priority, physics_service, game_over):
        self._physics_service = physics_service
        self._game_over = game_over
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")

        for bird in actors.get_actors("birds"):
            if self._physics_service.check_collision(bird, player):
                player.set_vx(bird.get_vx()*4)
                actors.remove_actor("birds", bird)
                #actors.add_actor("game_over", self._game_over)
 
        for base_platform in actors.get_actors("limit_platforms"):
            if self._physics_service.check_collision(base_platform, player) and self._physics_service.is_above(player, base_platform):
                base_platform_top = base_platform.get_top_left()[1]
                player.set_y(base_platform_top - (player.get_height() / 2))
                player.set_vy(0)
                airborne = False
                # actors.remove_actor("player", player)
                actors.add_actor("game_over", self._game_over)
                #player.set_airborne(False)
 