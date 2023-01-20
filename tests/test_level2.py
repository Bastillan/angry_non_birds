from src.level2 import Level2
import pygame


def test_level_create():
    pygame.init()
    window = pygame.display.set_mode((1500, 800))
    level2 = Level2(window)
    assert level2.tries == 3
    assert level2.number_of_bodies == 7
    assert level2.number_of_targets == 3
