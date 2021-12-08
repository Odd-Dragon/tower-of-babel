from genie.script.action import Action

class UpdateScreenAction(Action):
    def __init__(self, priority, screen_service):
        self._screen_service = screen_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._screen_service.update_screen()
