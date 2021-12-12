from genie.script.action import Action

class RemovePlatformAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        platforms = actors.get_actors("platforms")
        for platform in platforms:
            if platform.get_y() > 900:
                actors.remove_actor("platforms", platform)
