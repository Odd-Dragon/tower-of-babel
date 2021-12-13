#Taco
from genie.script.action import Action
from jumpingDemo.cast.feather_display import FeatherDisplay
#from main import W_SIZE
W_SIZE = (600, 800)

class PlayerFeatherCollisionAction(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        MAX_FEATHERS = 5
        feathers = actors.get_actors("feathers")
        player = actors.get_first_actor("player")
        position_number = player.get_feathers()
        if position_number <= MAX_FEATHERS:
            for feather in feathers:
                if self._physics_service.check_collision(feather, player):
                    position_number = player.get_feathers()
                    player.add_a_feather()
                    feather_display = FeatherDisplay("resources/feather.png", 40, 40, W_SIZE[0] - 30, W_SIZE[1] - 30, 0, 0, 0, 0, False)
                    feather_display.set_position_number(position_number)
                    actors.remove_actor("feathers", feather)
                    actors.add_actor("feather_display", feather_display)
