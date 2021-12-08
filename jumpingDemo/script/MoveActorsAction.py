from genie.script.action import Action

GRAVITY = 1

class MoveActorsAction(Action):
    def __init__(self, priority, physics_service):
        self._physics_service = physics_service
        super().__init__(priority)

    def execute(self, actors, actions, clock, callback):
        self._physics_service.move_actors(actors.get_all_actors())
            