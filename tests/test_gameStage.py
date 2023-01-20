from src.gameStage import GameStage
import pygame


def test_gamestage_create():
    pygame.init()
    window = pygame.display.set_mode((120, 60))
    gameStage = GameStage(window)
    assert gameStage.wall_color == 'white'
    assert gameStage.window == window
    assert gameStage.width == 120
    assert gameStage.height == 60
