import time
from genie.cast.actor import Actor
from genie.script.action import UpdateAction
import random as rd
SPAWN_INTERVAL = 2

class SpawnPlatformAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
       
        self._last_spawn = time.time()
        
        
    def _create_platforms(self, width:int, height:int, x:int, y:int):
        return Actor("genie/assets/platform.png", width, height, x, y, vy=1.5)

    def execute(self, actors, actions, clock, callback):
        width = rd.randint(200,300)
        height = 20
        y = 0
        x = rd.randint(100, 500)
        if time.time() - self._last_spawn >= SPAWN_INTERVAL:
            platform = self._create_platforms(width, height, x, y)
            actors.add_actor("platform", platform)
            self._last_spawn = time.time()
            



            