from genie.cast.actor import Actor

class Player(Actor):
    def __init__(self, paths: list, width: int, height: int, 
                    animation_fps : int = 10, game_fps : int = 60,
                    event_triggered : bool = True,
                    x: float = 0, y: float = 0, 
                    vx: float = 0, vy: float = 0, 
                    rotation: float = 0, rotation_vel: float = 0, 
                    flipped: bool = False):
    #Animation attributes
        self._paths = paths
        self._animation_speed = float(animation_fps) / float(game_fps)
        self._is_animating = True
        self._event_triggered = event_triggered
        self._current_frame = 0
    #Other attributes   
        self._is_airborne = True
        self._has_dash = True
        self._can_throw_dounut = True
        self._is_facing_right = True
        self._feathers = 0
        self._MAX_FALLSPEED_RESET_TO = 10
        self._max_fallspeed = self._MAX_FALLSPEED_RESET_TO
        super().__init__(paths[0], width, height, x=x, y=y, 
                            vx=vx, vy=vy, rotation=rotation, 
                            rotation_vel=rotation_vel, flipped=flipped)
    

    #Methods to handle animation of the player:
    def get_paths(self):
        return self._paths
    
    def set_paths(self, paths):
        self._paths = paths
    
    def get_current_path(self):
        return self._paths[int(self._current_frame)]

    def get_animation_speed(self):
        return self._animation_speed
    
    def set_animation_speed(self, animation_speed : float):
        self._animation_speed = animation_speed
    
    def is_animating(self):
        return self._is_animating

    def set_animating(self, animating : bool):
        self._is_animating = animating
    
    def set_next_frame(self):
        if self._is_animating:
            self._current_frame += self._animation_speed
        
            if int(self._current_frame) >= len(self._paths):
                self._current_frame = 0
                if self._event_triggered:
                    self._is_animating = False
            
            self._path = self._paths[int(self._current_frame)]

    #Other methods        
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