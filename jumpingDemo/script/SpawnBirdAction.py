from genie.script.action import Action
from jumpingDemo.cast.bird import Bird

class SpawnBirdAction(Action):
    def __init__(self, priority):
        self._frame = 0
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._frame += 1
        if self._frame == 60:
            bird = Bird("", 50, 50, 0, 400, 10, 0)
            actors.add_actor("birds", bird)
            self._frame = 0
        
