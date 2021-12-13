from genie.cast.actor import Actor
from genie.cast.animatedActor import AnimatedActor

class Player(AnimatedActor):
    def __init__(self, paths: list, width: int, height: int, 
                    animation_fps : int = 1, game_fps : int = 60,
                    event_triggered : bool = True,
                    x: float = 0, y: float = 0, 
                    vx: float = 0, vy: float = 0, 
                    rotation: float = 0, rotation_vel: float = 0, 
                    flipped: bool = False):
    #Other attributes   
        self._is_airborne = True
        self._has_dash = True
        self._can_throw_dounut = True
        self._is_facing_right = True
        self._feathers = 0
        self._MAX_FALLSPEED_RESET_TO = 10
        self._max_fallspeed = self._MAX_FALLSPEED_RESET_TO
        super().__init__(paths, width, height,  
                            animation_fps, game_fps,
                            event_triggered, x=x, y=y, 
                            vx=vx, vy=vy, rotation=rotation, 
                            rotation_vel=rotation_vel, flipped=flipped)
    
    def get_airborne(self):
        return self._is_airborne
    
    def set_airborne(self, airborne):
        self._is_airborne = airborne

    def get_has_dash(self):
        return self._has_dash
    
    def set_has_dash(self, dash:bool):
        self._has_dash = dash
    
    def get_can_throw_dounut(self):
        return self._can_throw_dounut
    
    def set_can_throw_dounut(self, new:bool):
        self._can_throw_dounut = new
    
    def get_is_facing_right(self):
        return self._is_facing_right
    
    def set_is_facing_right(self, new:bool):
        self._is_facing_right = new
        #self.flipped = not self._is_facing_right

    def get_feathers(self):
        return self._feathers

    def add_a_feather(self):
        self._feathers += 1

    def remove_a_feather(self):
        self._feathers -= 1

    def get_max_fallspeed(self):
        return self._max_fallspeed

    def set_max_fallspeed(self, fallspeed):
        self._max_fallspeed = fallspeed

    def get_max_fallspeed_reset_to(self):
        return self._MAX_FALLSPEED_RESET_TO