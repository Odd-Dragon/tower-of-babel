from genie.script.action import Action

class RemoveBackgroundAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        background = actors.get_actors("background")
        for background in background:
            if background.get_y() == 1400:
                actors.remove_actor("background", background)
