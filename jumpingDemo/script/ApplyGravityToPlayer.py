from genie.script.action import Action

GRAVITY = 0.3

class ApplyGravtityToPlayer(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        if player.get_airborne():
            if player.get_vy() < player.get_max_fallspeed():
                player.set_vy(player.get_vy() + GRAVITY)
        else:
            player.set_vy(player.get_difficulty()+0.5)
