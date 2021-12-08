from genie.script.action import Action

GRAVITY = 1

class HandlePlayerJumpOnSidesOfPlatform(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        for platform in actors.get_actors("platform"):
            if self._physics_service.check_collision(platform, player):
                # If collides from the left or right, prevents player from going through platform

                if self._physics_service.is_left_of(player, platform):
                    platform_left = platform.get_top_left()[0]
                    player.set_x(platform_left - (player.get_width() / 2))

                if self._physics_service.is_right_of(player, platform):
                    platform_right = platform.get_top_right()[0]
                    player.set_x(platform_right + (player.get_width() / 2))