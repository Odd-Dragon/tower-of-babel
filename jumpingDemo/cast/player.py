from genie.cast.actor import Actor

class Player(Actor):
    def __init__(self, path: str, width: int, height: int, x: float = 0, y: float = 0, vx: float = 0, vy: float = 0, rotation: float = 0, rotation_vel: float = 0, flipped: bool = False):
        self._is_airborne = True
        self._has_dash = True
        self._can_throw_dounut = True
        self._is_facing_right = True
        super().__init__(path, width, height, x=x, y=y, vx=vx, vy=vy, rotation=rotation, rotation_vel=rotation_vel, flipped=flipped)\
    
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