from genie.script.action import Action

GRAVITY = 1

class ApplyGravtityToPlayer(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        player = actors.get_first_actor("player")
        player.set_vy(player.get_vy() + GRAVITY)
