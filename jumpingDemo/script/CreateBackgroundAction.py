from genie.cast.actor import Actor
from genie.cast.cast import Cast
from genie.script.action import Action
from jumpingDemo.script.SpawnPlatformAction import SPAWN_INTERVAL

class CreateBackgroundAction(Action):
    def __init__(self, priority, window_size):
        self._window_size = window_size
        super().__init__(priority)   
        


    def execute(self, actors, actions, clock, callback):

        x = 400
        y = -499
        
        # background = Actor("resources/background.png", 600, 900, x, y,  vy=1)
        backgrounds = actors.get_actors("background")
        for background in backgrounds:
            background_position = background.get_position()[1]
            if background_position == 400:
                new_background = Actor("resources/background.png", 600, 900, x, y, vy=1)
                actors.add_actor("background", new_background )
            
 
        
            



                        