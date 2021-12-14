from genie.cast.actor import Actor
from genie.cast.animatedActor import AnimatedActor
from genie.cast.actor import Actor

class Bird(AnimatedActor):
    def __init__(self, path, width: int, height: int, animation_fps : int = 1, game_fps : int = 60, event_triggered : bool = True, x: float = 0, 
    y: float = 0, vx: float = 0, vy: float = 0, rotation: float = 0, 
    rotation_vel: float = 0, flipped: bool = False):
        super().__init__(path, width, height, animation_fps, game_fps, event_triggered, x=x, y=y, vx=vx, vy=vy, rotation=rotation, rotation_vel=rotation_vel, flipped=flipped)\
