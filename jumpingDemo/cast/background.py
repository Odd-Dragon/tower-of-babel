from genie.cast.actor import Actor

class Background(Actor):
    def __init__(self, path, x: float = 0, y: float = 0, vy: float = 0):
        super().__init__(path, 600, 900, x, y, vy)