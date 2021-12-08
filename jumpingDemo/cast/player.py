from genie.cast.actor import Actor

class Player(Actor):
    def __init__(self, path: str, width: int, height: int, x: float = 0, y: float = 0, vx: float = 0, vy: float = 0, rotation: float = 0, rotation_vel: float = 0, flipped: bool = False):
        self._is_airborne = True
        super().__init__(path, width, height, x=x, y=y, vx=vx, vy=vy, rotation=rotation, rotation_vel=rotation_vel, flipped=flipped)\
    
    def get_airborne(self):
        return self._is_airborne
    
    def set_airborne(self, airborne):
        self._is_airborne = airborne