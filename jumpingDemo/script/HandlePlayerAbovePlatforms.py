from genie.script.action import Action

GRAVITY = 1

class HandlePlayerAbovePlatforms(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        #print(player.get_vy())
        airborne = True
        for platform in actors.get_actors("platform"):
            if self._physics_service.check_collision(platform, player) and self._physics_service.is_above(player, platform):
                platform_top = platform.get_top_left()[1]
                player.set_y(platform_top - (player.get_height() / 2))
                player.set_vy(0)
                airborne = False
                #player.set_airborne(False)
        for base_platform in actors.get_actors("base_platform"):
            if self._physics_service.check_collision(base_platform, player) and self._physics_service.is_above(player, base_platform):
                base_platform_top = base_platform.get_top_left()[1]
                player.set_y(base_platform_top - (player.get_height() / 2))
                player.set_vy(0)
                airborne = False
                #player.set_airborne(False)
            player.set_airborne(airborne)