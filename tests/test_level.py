from src.level import Level
import pygame
import pymunk


def test_level_create():
    pygame.init()
    window = pygame.display.set_mode((120, 60))
    level = Level(window)
    assert level.wall_color == 'white'
    assert level.window == window
    assert level.width == 120
    assert level.height == 60
    assert isinstance(level.space, pymunk.Space) is True
    assert level.ball is None
    assert level.tries == 1
    assert level.number_of_targets == 0
    assert level.number_of_bodies == 0
