#Taco
from genie.script.action import Action
from jumpingDemo.cast.feather import Feather

class DounutBirdCollisionAction(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        birds = actors.get_actors("birds")
        dounuts = actors.get_actors("dounuts")
        player = actors.get_first_actor("player")
        for bird in birds:
            for dounut in dounuts:
                if self._physics_service.check_collision(bird, dounut):
                    feather = Feather("resources/feather.png", 30, 30, bird.get_x(), bird.get_y(), 0, player.get_difficulty(), 0, 0, False)
                    actors.remove_actor("birds", bird)
                    actors.remove_actor("dounuts", dounut)
                    actors.add_actor("feathers", feather)
