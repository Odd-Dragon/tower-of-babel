from genie.script.action import Action

class DrawActorAction(Action):
    def __init__(self, priority, screen_service):
        self._screen_service = screen_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._screen_service.fill_screen()
        all_actors = actors.get_all_actors()
        for actor in all_actors:
            self._screen_service.draw_rectangle(actor.get_position(), actor.get_width(), actor.get_height(), (0,0,0, 255), 5)
