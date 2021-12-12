from genie.script.action import Action

class MoveBackgroundAction(Action):
    def __init__(self, priority):
        super().__init__(priority)

    def execute(self, cast, actions, clock, callback):
        backgrounds = cast.get_actors("background")
        background = backgrounds[:1][0]
        background1 = backgrounds[:2]
        if background.get_x() > 800:
            backgrounds.remove(background)
            backgrounds.insert(0, background)
            background.set_x(background1.get_x()- 600)
            