from random import randint
from globals import *
from jumpingDemo.script.DrawActorAction import DrawActorAction
from jumpingDemo.script.HandleJumpingAction import HandleJumpingAction
from jumpingDemo.script.HandleQuitAction import HandleQuitAction
from jumpingDemo.script.HandleStartGameAction import HandleStartGameAction
from jumpingDemo.script.RemovePlatformAction import RemovePlatformAction
from jumpingDemo.script.SpawnBirdAction import SpawnBirdAction
from jumpingDemo.script.RemoveBirdAction import RemoveBirdAction
from jumpingDemo.script.UpdateScreenAction import UpdateScreenAction
from jumpingDemo.script.ApplyGravityToPlayer import ApplyGravtityToPlayer
from jumpingDemo.script.MoveActorsAction import MoveActorsAction
from jumpingDemo.script.HandlePlayerAbovePlatforms import HandlePlayerAbovePlatforms
from jumpingDemo.script.HandlePlayerMovementAction import HandlePlayerMovementAction
from jumpingDemo.script.HandlePlayerJumpOnSidesOfPlatform import HandlePlayerJumpOnSidesOfPlatform
from jumpingDemo.script.HandlePlayerJumpAtBottomOfPlatform import HandlePlayerJumpAtBottomOfPlatform
from jumpingDemo.script.MoveBackgroundAction import MoveBackgroundAction
from jumpingDemo.script.SpawnPlatformAction import SpawnPlatformAction
from jumpingDemo.script.ThrowDounutAction import ThrowDounutAction
from jumpingDemo.script.HandleDounutsAction import HandleDounutsAction
from jumpingDemo.script.DounutBirdCollisionAction import DounutBirdCollisionAction
from jumpingDemo.script.PlayerFeatherCollisionAction import PlayerFeatherCollisionAction
from jumpingDemo.script.PlayerTimerAction import PlayerTimerAction
from jumpingDemo.script.HandleGameOver import GameOver
from jumpingDemo.script.PlayBackgroundMusic import PlayBackgroundMusicAction
from jumpingDemo.script.CreateBackgroundAction import CreateBackgroundAction
from jumpingDemo.script.RemoveBackgroundAction import RemoveBackgroundAction


from genie.cast.cast import Cast
from genie.cast.actor import Actor
from genie.script.script import Script

from genie.director import Director

from genie.services import *
from jumpingDemo.cast.player import Player
from jumpingDemo.cast.feather import Feather
from jumpingDemo.cast.background import Background
from jumpingDemo.cast.startGameButton import StartGameButton

MAX_FPS = 120
def main():
    
    screen_service = RaylibScreenService(W_SIZE)
    physics_service = RaylibPhysicsService()
    keyboard_service = RaylibKeyboardService()
    audio_service = RaylibAudioService()
    mouse_service = RaylibMouseService()

    director = Director()

    cast = Cast()
    
    #Add the animated Player:
      

    player_animations = []
    for i in range(1, 3):
        
        player_animations.append(f"resources/zombie{i}.png")
    PLAYER_START_X = W_SIZE[0] - 800
    PLAYER_START_Y = 500
    player = Player(player_animations, 50, 65, 30, MAX_FPS, True, PLAYER_START_X, PLAYER_START_Y)
    feather1 = Feather("resources/feather.png", 30, 30, PLAYER_START_X, PLAYER_START_Y, 0, 0, 0, 0, False)
    feather2 = Feather("resources/feather.png", 30, 30, PLAYER_START_X, PLAYER_START_Y, 0, 0, 0, 0, False)
    feather3 = Feather("resources/feather.png", 30, 30, PLAYER_START_X, PLAYER_START_Y, 0, 0, 0, 0, False)
    limit_top = Actor("resources/platform.png", W_SIZE[0], 400, W_SIZE[0]/2, -200)
    limit_bottom = Actor("", W_SIZE[0]+100, 400, W_SIZE[0]/2, W_SIZE[1]+200)

  
                               
                                
    difficulty = player.get_difficulty()
    limit_left = Actor("", 600, W_SIZE[1]+100, W_SIZE[0] -1380, W_SIZE[1]/2)
    limit_right = Actor("", 600, W_SIZE[1]+100, W_SIZE[0]+177, W_SIZE[1]/2)
    # "" Width Height X Y
    platform1 = Actor("resources/platform.png", 400, 20, 400, 600, vy=difficulty)
    platform2 = Actor("resources/platform.png", 400, 20, 800, 450, vy=difficulty)
    platform3 = Actor("resources/platform.png", 400, 20, 600, 300, vy=difficulty)
    platform4 = Actor("resources/platform.png", 400, 20, 500, 150, vy=difficulty)
    platform5 = Actor("resources/platform.png", 400, 20, 800, 0, vy=difficulty)
    
    # background_x = W_SIZE[0]/2
    # background_y = W_SIZE[1]/5
    # background1 = Background(background_x,0)
    # background2 = Background(background_x,background_y)
    # background3 = Background(background_x,background_y*2)
    # background4 = Background(background_x,background_y*3)
    # background5 = Background(background_x,background_y*4)
    # background6 = Background(background_x,background_y*5)

    background1 = Actor("resources/background.png", 1000, 750, W_SIZE[0] / 2, 375,  vy=1)
    static_image = Actor("resources/forest.png", 1200, 750,  W_SIZE[0] / 2, W_SIZE[1] /2)
    
    start_button = Actor("resources/start_game_button.png", 305, 51, W_SIZE[0]/2, 300)
    game_over = Actor("resources/game_over.png", 305, 51, W_SIZE[0]/2, 300)
    
    cast.add_actor("static_image", static_image)
    cast.add_actor("background", background1)
    # cast.add_actor("background", background1)
    # cast.add_actor("background", background2)
    # cast.add_actor("background", background3)
    # cast.add_actor("background", background4)
    # cast.add_actor("background", background5)
    # cast.add_actor("background", background6)
    cast.add_actor("player", player)
    cast.add_actor("feathers", feather1)
    cast.add_actor("feathers", feather2)
    cast.add_actor("feathers", feather3)
    cast.add_actor("limit_platforms", limit_top)
    cast.add_actor("limit_platforms", limit_bottom)
    cast.add_actor("limit_platforms", limit_left)
    cast.add_actor("limit_platforms", limit_right)
    cast.add_actor("platforms", platform1)
    cast.add_actor("platforms", platform2)
    cast.add_actor("platforms", platform3)
    cast.add_actor("platforms", platform4)
    cast.add_actor("platforms", platform5)
    cast.add_actor("start_button", start_button)
    
    
    script = Script()

    startgame_actions = {"input" : [], "update" : [], "output": []}
    startgame_actions["input"].append(HandleJumpingAction(1, keyboard_service, audio_service))
    startgame_actions["input"].append(HandlePlayerMovementAction(1, keyboard_service))
    startgame_actions["input"].append(SpawnBirdAction(1))
    startgame_actions["input"].append(ThrowDounutAction(1, keyboard_service, audio_service))
    startgame_actions["input"].append(CreateBackgroundAction(1, W_SIZE))
    startgame_actions["input"].append(MoveActorsAction(1, physics_service))
    startgame_actions["update"].append(SpawnPlatformAction(1, physics_service))

    
    


    
    script.add_action("input", HandleStartGameAction(2, mouse_service, physics_service, startgame_actions))
    script.add_action("input", HandleQuitAction(1, keyboard_service))

   
    
    
    script.add_action("update", HandlePlayerAbovePlatforms(1, physics_service, game_over))
    script.add_action("update", HandlePlayerJumpAtBottomOfPlatform(1, physics_service))
    script.add_action("update", HandlePlayerJumpOnSidesOfPlatform(1, physics_service))
    script.add_action("update", ApplyGravtityToPlayer(2))
    script.add_action("update", RemoveBirdAction(1))
    # script.add_action("update", MoveBackgroundAction(1))
    script.add_action("update", RemovePlatformAction(1))
    script.add_action("update", RemoveBackgroundAction(1))
    script.add_action("update", HandleDounutsAction(1))
    script.add_action("update", DounutBirdCollisionAction(1, physics_service))
    script.add_action("update", PlayerFeatherCollisionAction(1, physics_service))
    script.add_action("update", PlayerTimerAction(1))
    script.add_action("update", GameOver(1, physics_service, game_over))


    script.add_action("output", PlayBackgroundMusicAction(2, "resources/background_music.wav", audio_service))
    script.add_action("output", DrawActorAction(1, screen_service))
    script.add_action("output", UpdateScreenAction(2, screen_service))
    
    director.direct_scene(cast, script)




if __name__ == "__main__":
    main()