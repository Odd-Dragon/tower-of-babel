from genie.script.action import Action

GRAVITY = 1

class HandlePlayerJumpAtBottomOfPlatform(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        print(player.get_vy())
        for platform in actors.get_actors("platform"):
            if self._physics_service.check_collision(platform, player) and self._physics_service.is_below(player, platform):
                # If collides from the left or right, prevents player from going through platform
                platform_bottom = platform.get_bottom_left()[1]
                player.set_y(platform_bottom + (player.get_height() / 2))
                player.set_vy(0) #set the velocity = 0 so it starts to fall