from genie.script.action import Action

class HandleDounutsAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        GRAVITY = 0.4
        dounuts = actors.get_actors("dounuts")
        for dounut in dounuts:
            dounut.set_vy(dounut.get_vy()+GRAVITY)
            if dounut.get_y() > 900:
                actors.remove_actor("dounuts", dounut)
