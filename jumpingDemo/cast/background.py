from genie.cast.actor import Actor
from globals import *
class Background(Actor):
    def __init__(self, x: float = 0, y: float = 0, vy: float = 1.5):
        PARRALAX = 2
        super().__init__("resources/mudbricks.png", W_SIZE[0], (W_SIZE[1]/5)+2, x=x, y=y, vx = 0, vy = vy/PARRALAX)
