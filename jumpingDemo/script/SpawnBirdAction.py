from genie.script.action import Action
from jumpingDemo.cast.bird import Bird
from random import randint
from globals import *

class SpawnBirdAction(Action):
    def __init__(self, priority):
        self._frame = 0
        self._threshold = 80
        self._speed = 2
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._frame += 1
        if self._frame >= self._threshold:
            left_or_right_spawn = randint(0, 1) * W_SIZE[0]
            vertical_spawn_point = randint(100, W_SIZE[0]-100)
            if left_or_right_spawn == 0:
                bird_velocity = self._speed
            else:
                bird_velocity = -self._speed
            bird_animations = []
            for i in range(1, 4):
                bird_animations.append(f"resources/bird{i}.png")
                    
            bird = Bird(bird_animations, 50, 40, 3, 30, False,  left_or_right_spawn, vertical_spawn_point, bird_velocity, 0)
            if left_or_right_spawn  is not 0:
                bird.flip_image()
            actors.add_actor("birds", bird)
            self._frame = 0
            player = actors.get_first_actor("player")
            self._threshold = 80/player.get_difficulty()
            self._speed = 2*player.get_difficulty()

