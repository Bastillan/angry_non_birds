from src.credits import Credits
import pygame


def test_credits_create_default():
    pygame.init()
    window = pygame.display.set_mode((120, 60))
    credits = Credits(window)
    assert credits.wall_color == 'red'
    assert credits.window == window
    assert credits.width == 120
    assert credits.height == 60
    assert credits.text == 'Credits'


def test_credits_create():
    pygame.init()
    window = pygame.display.set_mode((120, 60))
    credits = Credits(window, 'Win')
    assert credits.wall_color == 'red'
    assert credits.window == window
    assert credits.width == 120
    assert credits.height == 60
    assert credits.text == 'Win'
