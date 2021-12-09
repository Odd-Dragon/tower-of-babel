from genie.script.action import Action
from jumpingDemo.cast.bird import Bird
from random import randint

class SpawnBirdAction(Action):
    def __init__(self, priority):
        self._frame = 0
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._frame += 1
        if self._frame == 80:
            left_or_right_spawn = randint(0, 1) * 600
            vertical_spawn_point = randint(100, 700)
            if left_or_right_spawn == 0:
                bird_velocity = 10
            elif left_or_right_spawn == 600:
                bird_velocity = -10
            bird = Bird("", 50, 40, left_or_right_spawn, vertical_spawn_point, bird_velocity, 0)
            actors.add_actor("birds", bird)
            self._frame = 0
