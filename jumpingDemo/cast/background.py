from genie.cast.actor import Actor

class Background(Actor):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__("genie/assets/background.png", 600, 600, x=x, y=y)