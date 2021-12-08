from jumpingDemo.script.DrawActorAction import DrawActorAction
from jumpingDemo.script.HandleJumpingAction import HandleJumpingAction
from jumpingDemo.script.HandleQuitAction import HandleQuitAction
from jumpingDemo.script.UpdateScreenAction import UpdateScreenAction
from jumpingDemo.script.ApplyGravityToPlayer import ApplyGravtityToPlayer
from jumpingDemo.script.MoveActorsAction import MoveActorsAction
from jumpingDemo.script.HandlePlayerAbovePlatforms import HandlePlayerAbovePlatforms
from jumpingDemo.script.HandlePlayerMovementAction import HandlePlayerMovementAction
from jumpingDemo.script.HandlePlayerJumpOnSidesOfPlatform import HandlePlayerJumpOnSidesOfPlatform
from jumpingDemo.script.HandlePlayerJumpAtBottomOfPlatform import HandlePlayerJumpAtBottomOfPlatform

from genie.cast.cast import Cast
from genie.cast.actor import Actor
from genie.script.script import Script

from genie.director import Director

from genie.services import *
from jumpingDemo.cast.player import Player


W_SIZE = (600, 800)

def main():
    
    screen_service = RaylibScreenService(W_SIZE)
    physics_service = RaylibPhysicsService()
    keyboard_service = RaylibKeyboardService()

    director = Director()

    cast = Cast()

    player = Player("", 50, 50, 100, 400)
    platform1 = Actor("", 600, 400, 300, 800)
    platform2 = Actor("", 150, 100, 400, 375)
    platform3 = Actor("", 150, 50, 120, 450)
    
    cast.add_actor("player", player)
    cast.add_actor("platform", platform1)
    cast.add_actor("platform", platform2)
    cast.add_actor("platform", platform3)

    script = Script()

    script.add_action("input", HandleQuitAction(1, keyboard_service))
    script.add_action("input", HandleJumpingAction(1, keyboard_service))
    script.add_action("input", HandlePlayerMovementAction(1, keyboard_service))


    script.add_action("update", MoveActorsAction(1, physics_service))
    script.add_action("update", HandlePlayerAbovePlatforms(1, physics_service))
    script.add_action("update", HandlePlayerJumpAtBottomOfPlatform(1, physics_service))
    script.add_action("update", HandlePlayerJumpOnSidesOfPlatform(1, physics_service))
    script.add_action("update", ApplyGravtityToPlayer(2))


    script.add_action("output", DrawActorAction(1, screen_service))
    script.add_action("output", UpdateScreenAction(2, screen_service))
    
    director.direct_scene(cast, script)




if __name__ == "__main__":
    main()