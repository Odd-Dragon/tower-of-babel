from genie.script.action import Action

class RemoveBirdAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        birds = actors.get_actors("birds")
        for bird in birds:
            if bird.get_x() > 1000 or bird.get_x() < -30:
                actors.remove_actor("birds", bird)
