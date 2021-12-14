from genie.script.action import Action
from jumpingDemo.cast.bird import Bird
from random import randint

class SpawnBirdAction(Action):
    def __init__(self, priority):
        self._frame = 0
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._frame += 1
        bird_animations = []
        for i in range(1, 4):
            bird_animations.append(f"resources/bird{i}.png")
                
        if self._frame == 150:
            left_or_right_spawn = randint(0, 1) * 800
            vertical_spawn_point = randint(100, 600)
            if left_or_right_spawn == 0:
                bird_velocity = 3
                
            else:
                bird_velocity = -3
                
          

                         
            bird = Bird(bird_animations, 50, 40, 3, 30, False,  left_or_right_spawn, vertical_spawn_point, bird_velocity, 0)
            if left_or_right_spawn  is not 0:
                bird.flip_image()
            actors.add_actor("birds", bird)
            self._frame = 0
