import time
from genie.cast.actor import Actor
from genie.script.action import UpdateAction
import random as rd
from globals import *


class SpawnPlatformAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._spawn_interval = 2
        self._last_spawn = time.time()
        
        
    def _create_platforms(self, width:int, height:int, x:int, y:int, vy:float = 1.5):
        return Actor("resources/platform.png", width, height, x, y, vy=vy)

    def execute(self, actors, actions, clock, callback):   
        if time.time() - self._last_spawn >= self._spawn_interval:
            player = actors.get_first_actor("player")
            player.increment_difficulty()
            if self._spawn_interval > 1:
                self._spawn_interval *= 0.997
            width = rd.randint(400,550)
            height = 20
            y = 0
            x = rd.randint(400, W_SIZE[0]-400)
            platform = self._create_platforms(width, height, x, y, vy = player.get_difficulty())
            actors.add_actor("platforms", platform)
            self._last_spawn = time.time()
            



            