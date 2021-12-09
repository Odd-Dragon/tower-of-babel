from genie.script.action import Action

GRAVITY = 0.5

class ApplyGravtityToPlayer(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        if player.get_airborne():
            player.set_vy(player.get_vy() + GRAVITY)
        else:
            player.set_vy(2)
